import torch
 
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#hyper parameters

hidden_size = 128
num_classes = 10
num_epochs = 2
batch_size = 100
learning_rate = 0.005
input_size = 28
sequence_length = 28
num_layers = 2

train_dateset = torchvision.datasets.MNIST(root='./data', train=True, transform=transforms.ToTensor(), download=True)   
test_dataset = torchvision.datasets.MNIST(root='./data', train=False, transform=transforms.ToTensor(), download=True)


train_loader = torch.utils.data.DataLoader(dataset=train_dateset, batch_size=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)

class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super(LSTM, self).__init__()
        self.num_layers = num_layers
        self.hidden_size= hidden_size
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        # x->(batch_size,senquence, feature) if the batch_first is true
        self.fc = nn.Linear(hidden_size, num_classes)
    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        
        out,_ = self.lstm(x, (h0,c0))
        out = out[:, -1, :]
        out = self.fc(out)
        return out
    

model = LSTM(input_size, hidden_size, num_layers, num_classes).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

n_total_steps = len(train_loader)
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):
        #100, 1, 28, 28
        images = images.reshape(-1, sequence_length, input_size).to(device)
        labels = labels.to(device)
        #forward
        outputs = model(images)
        loss = criterion(outputs, labels)
        #backward
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if (i+1)%100 == 0:
            print(f'Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{n_total_steps}], Loss: {loss.item():.4f}')


#test
with torch.no_grad():
    n_correct = 0
    n_samples = 0
    for images, labels in test_loader:
        #100, 1, 28, 28
        images = images.reshape(-1, sequence_length, input_size).to(device)
        labels = labels.to(device)
        #forward
        outputs = model(images)
        #value, index
        _, predictions = torch.max(outputs, 1)
        n_samples += labels.shape[0]
        n_correct += (predictions == labels).sum().item()
    acc = 100.0 * n_correct / n_samples
    print(f'accuracy = {acc}')