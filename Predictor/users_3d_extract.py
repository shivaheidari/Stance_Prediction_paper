import os
import json
import pandas as pd
import numpy as np
import sys
import get_users_friends as guf


time_window = 7

users_active = open("./Data/Galaxy_ds/seed_users_active.txt").read().splitlines()
tweet_dir = "./Data/Galaxy_ds/W2Vec/Seed_users_target_tweets/Opinion_word_vec/"

network = guf.get_network()



class user_features:
    def __init__(self,username):
        self.username = username
        self.user_file = tweet_dir + username + ".json"
        print(self.user_file)
        self.user_tweets = self.get_tweets(self.user_file)


    def get_tweets(self, user_file):
        if os.path.exists(user_file) == True:
            data = []
            with open(user_file) as f:
                for line in f:
                    data.append(json.loads(line))
            user_tweets = pd.DataFrame(data)
            user_tweets["datetime"] = pd.to_datetime(user_tweets["created_at"], unit="ms")
            return user_tweets
        else:
            return "empty"

    def vector_summation(self, vector_df):
        if vector_df.empty == True:
            return  "empty"
        final_vector = np.zeros(len(vector_df.iloc[0]["vector"]))
        for _,row in vector_df.iterrows():
            final_vector = np.add(final_vector, row["vector"])
        return final_vector
    
    def get_history(self,target_history):
        target_history_df = self.user_tweets[self.user_tweets["datetime"] < target_history]
        history = self.vector_summation(target_history_df)
        return history

    def get_prior(self,target_history, target_prior):
        target_prior_df = user_tweets[user_tweets["datetime"].between(target_history, target_prior)]
        prior = self.vector_summation(target_prior_df)
        return prior
    

    def get_friends_stance(self,target_history,upper_bound):
        target_friends = self.get_friends(self.username, network)
        if target_friends == "empty":
            return "empty"
        all_friends_vectors = pd.DataFrame({"vector":[]})
        for friend in target_friends:
            friend_file = tweet_dir + friend[0] + ".json"
    
            if os.path.exists(friend_file) == True:
                data = []
                with open(friend_file) as f:
                    for line in f:
                        data.append(json.loads(line))
            else:
                 continue
            friend_tweets = pd.DataFrame(data)
            friend_tweets["datetime"] = pd.to_datetime(friend_tweets["created_at"], unit="ms")
            friend_tweets = friend_tweets[friend_tweets["datetime"].between(target_history, upper_bound)]


    def get_friends(self, user, network_dict):
        if user in network_dict:
            return network_dict[user]
        else:
            return "empty"



obj = user_features("blackfootdeals")
user_tweets = obj.user_tweets

for index,row in user_tweets.iterrows():
    target_history = row["datetime"] - pd.Timedelta(days=time_window)
    #history = obj.get_history(target_history)
    #prior = obj.get_prior(target_history, row["datetime"])
    friends_stance = obj.get_friends_stance(target_history, row["datetime"])
    print(friends_stance)






# for user in users_active:
#     #print(user)
#     #get the tweets for each user
#     user_file = "./Data/Galaxy_ds/W2Vec/Seed_users_target_tweets/" + user + ".json"
#     #for each tweet get the history,prionr and friends
    

