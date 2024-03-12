#I choose a user with enough tweets i want to get the opinion vector for them. including personal prior and history and friends current opinion
#blackfootdeals is my user lets try to get the opinion vector for them
import json
import os
import numpy as np
import pandas as pd
#read the file of the user tweets

time_window = 7
network_file = "./Data/Galaxy_ds/Implicit_Network/seed_network_0.8.txt"
user_network_dict = {}


#read the users file from active users
user_file = "./Data/Galaxy_ds/seed_users_active.txt"


def vector_summation(vector_df):
     if vector_df.empty == True:
            return  "empty"
     final_vector = np.zeros(len(vector_df.iloc[0]["vector"]))
     for _,row in vector_df.iterrows():
         final_vector = np.add(final_vector, row["vector"])
     return final_vector


with open(network_file) as network_file:
     
        for line in network_file:
            line = line.rstrip()
            user, friend, influence_score = line.split(" ")
            if user in user_network_dict:
                user_network_dict[user].append((friend, influence_score))
            else:
                    user_network_dict[user] = [(friend, influence_score)]


def get_friends(user, network_dict):
    if user in network_dict:
        return network_dict[user]
    else:
        return "empty"
    



usertweet = "./Data/Galaxy_ds/W2Vec/Seed_users_target_tweets/Opinion_word_vec/blackfootdeals.json"
if os.path.exists(usertweet) == True:
    data = []
    with open(usertweet) as f:
        for line in f:
            data.append(json.loads(line))
user_tweets = pd.DataFrame(data)
user_tweets["datetime"] = pd.to_datetime(user_tweets["created_at"], unit="ms")

target_friends = get_friends("blackfootdeals", user_network_dict)
#print("target_friends", target_friends)
for index, row in user_tweets.iterrows():
    target_history = row["datetime"] - pd.Timedelta(days=time_window)
    #print("target",target_history, "datetime",row["datetime"])
#--------------------------------history-------------------------
    target_history_df = user_tweets[user_tweets["datetime"] < target_history]
    history = vector_summation(target_history_df)
#--------------------------------prior---------------------------
    target_prior = user_tweets[user_tweets["datetime"].between(target_history, row["datetime"])]
    # print("target_prior", target_prior.shape)
    prior = vector_summation(target_prior)
    print("prior", prior)
#--------------------------------friends-------------------------
    all_friends_vectors = pd.DataFrame({"vector":[]})
    
    for friend in target_friends:
        #friends_sums = pd.DataFrame()
        friend_tweets = "./Data/Galaxy_ds/W2Vec/Seed_users_target_tweets/Opinion_word_vec/" + friend[0] + ".json"
        if os.path.exists(friend_tweets) == True:
            data = []
            with open(friend_tweets) as f:
                for line in f:
                    data.append(json.loads(line))
        else:
            continue
        friend_tweets = pd.DataFrame(data)
        friend_tweets["datetime"] = pd.to_datetime(friend_tweets["created_at"], unit="ms")
        friend_tweets = friend_tweets[friend_tweets["datetime"].between(target_history, row["datetime"])]
        if friend_tweets.shape[0] != 0:
            friend_vector = vector_summation(friend_tweets)
            friend_vector_df = pd.DataFrame({"vector":[friend_vector]})
            all_friends_vectors = pd.concat([all_friends_vectors, friend_vector_df], ignore_index=True)
            #print(all_friends_vectors.shape, all_friends_vectors.columns, type(all_friends_vectors))
            #all_friends_vectors = all_friends_vectors.append({'vector':friend_vector}, ignore_index=True)
    #print(all_friends_vectors.head())
    friends = vector_summation(all_friends_vectors)
    print("friends",friends)
