import pandas as pd
import numpy as np
import ast
from ast import literal_eval
import torch
import json
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import warnings
warnings.filterwarnings("ignore")

test_size = 0.2
users_1st_batch = "Data/Galaxy_ds/sample_users/sample10.csv"
result_file = "Report/resRnn.txt"
f = open(result_file, "w")
file = open(users_1st_batch, "r")
class OpinionsDataset(Dataset):
        def __init__(self, X, stance):
            self.X = X
            self.stance = stance

        def __len__(self):
            return len(self.X)

        def __getitem__(self, idx):
            return self.X[idx], self.stance[idx]


class SimpleRNN(nn.Module):
        def __init__(self, input_size, hidden_size, output_size):
            super(SimpleRNN, self).__init__()
            self.hidden_size = hidden_size
            self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
            self.fc = nn.Linear(hidden_size, output_size)

        def forward(self, x):
            out, _ = self.rnn(x)
            out = self.fc(out[:, -1, :])
            return out
        

for user in file.readlines():
    user = user.strip()
    print(user)
    user_file = "./Data/Galaxy_ds/users_training_vectors_3D/" + "json_"+user+ ".json"

    #read json file
    prior = []
    history = []
    friends = []
    stance = []

    with open(user_file, "r") as read_file:
        for line in read_file:
            user_data = json.loads(line)

            prior.append(user_data['prior'])
            history.append(user_data['history'])
            friends.append(user_data['friends_stance'])
            stance.append(user_data['stance'])

    #to tensor
    prior = torch.tensor(prior, dtype=torch.float32)
    history = torch.tensor(history, dtype=torch.float32)
    friends = torch.tensor(friends, dtype=torch.float32)
    stance = torch.tensor(stance, dtype=torch.long)
    maped_stance = stance + 1
    #
    X = torch.stack([prior, history, friends], dim=-1)
    X_train, X_test, stance_train, stance_test = train_test_split(X.numpy(), maped_stance.numpy(), test_size=test_size, random_state=42)
    X_train, X_test, stance_train, stance_test = (
        torch.from_numpy(X_train),
        torch.from_numpy(X_test),
        torch.from_numpy(stance_train),
        torch.from_numpy(stance_test)
    )
    
    train_dataset = OpinionsDataset(X_train, stance_train)
    test_dataset = OpinionsDataset(X_test, stance_test)
    
    input_size = X.shape[-1]
    hidden_size = 64
    output_size = 3


    model = SimpleRNN(input_size, hidden_size, output_size)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    batch_size = 32
    train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_dataloader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    num_epochs = 10
    f1_scores = []
    recall_scores = []
    precision_scores = []
    accuracy_scores = []
    for epoch in range(num_epochs):
        for inputs, labels in train_dataloader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            print("backward")
            loss.backward()
            optimizer.step()
        model.eval()
        all_predictions = []
        all_labels = []
        with torch.no_grad():
            for inputs, labels in test_dataloader:
                outputs = model(inputs)
                _, predictions = torch.max(outputs, 1)
                all_predictions.extend(predictions.cpu().numpy())
                all_labels.extend(labels.cpu().numpy())
                test_loss = criterion(outputs, labels)
        accuracy = accuracy_score(all_labels, all_predictions)
        accuracy_scores.append(accuracy)
        f1 = f1_score(all_labels, all_predictions, average='weighted')
        f1_scores.append(f1)
        precision = precision_score(all_labels, all_predictions, average='weighted')
        precision_scores.append(precision)
        recall = recall_score(all_labels, all_predictions, average='weighted')
        recall_scores.append(recall)

    print("Accuracy: ", np.mean(accuracy_scores))
    print("F1: ", np.mean(f1_scores))
    print("Precision: ", np.mean(precision_scores))
    print("Recall: ", np.mean(recall_scores))

    user_dict = {"user": user, "accuracy": np.mean(accuracy_scores), "f1": np.mean(f1_scores), "precision": np.mean(precision_scores), "recall": np.mean(recall_scores)}
    f.write(str(user_dict))
    f.write("\n")
    