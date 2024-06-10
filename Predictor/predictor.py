import json
import os
import pandas as pd
import datetime
import numpy as np
#open json file for each user 
#choose a time window 

time_window = 7
train_percent = 0.7 #70 percent for training
user_file= "./Data/Galaxy_ds/seed_users_active_test_sample.txt"
user_list = open(user_file).read().splitlines()
#make a dictionary like user: [(frined1, influence score), (frined2, influence score), ...]
user_network_dict = {}
# open network file 
network_file = "./Data/Galaxy_ds/Implicit_Network/seed_network_0.8.txt"



def vector_summation(vector_list):
     final_vector = np.zeros(len(vector_list.iloc[0]["vector"]))
     for _,row in vector_list.iterrows():
         final_vector = [x + y for x, y in zip(final_vector, row["vector"])]
     print(final_vector)
     return final_vector

def get_history_vector(user_tweets, t_target_deltat):
     
         history_tweets = user_tweets[user_tweets["created_at"]<t_target_deltat]
         #check if the history_tweets is empty or not
         if history_tweets.empty == True:
                print("history empty",c_sentiment, D_sentiment)
                return "empty"
         history_final_vector = vector_summation(history_tweets)
         return history_final_vector

def get_prior_vector(user_tweets, t_target_deltat, t_target):
         
         #prior_tweets = user_tweets[(user_tweets["created_at"]>=t_target_deltat) & (user_tweets["created_at"]<t_target)]
         prior_tweets = user_tweets[user_tweets["created_at"].between(t_target_deltat, t_target)]
         #print("prior_shape", prior_tweets.shape)
         if prior_tweets.empty == True:
                
                return "empty"
         prior_final_vector = vector_summation(prior_tweets)
         return prior_final_vector



#gets the users friends and their influence score
with open (network_file) as network_file:
    for line in network_file:
        line = line.rstrip()
        user, friend, influence_score = line.split(" ")
        if user in user_network_dict:
            user_network_dict[user].append((friend, influence_score))
        else:
                user_network_dict[user] = [(friend, influence_score)]

for user in user_list:

    print(user)
    user_training_file = "./Data/Galaxy_ds/users_training_vectors_3D/" + user + ".txt"
    user_trainng_file = open(user_training_file, 'w+')
    tweet_file = "./Data/Galaxy_ds/W2Vec/Seed_users_target_tweets/Opinion_word_vec/" + user + ".json"
    #user_tweets = pd.DataFrame(columns=["tweet_id", "tweet", "opinion_words", "c_sentiment", "D_sentiment", "created_at", "date", "time", "vector"])
    if os.path.exists(tweet_file) == True:
        data = []
        with open(tweet_file) as f:
                for line in f:
                    data.append(json.loads(line))
    else:
        continue           
    user_tweets = pd.DataFrame(data)
    #print(user_tweets.shape)
    user_tweets["created_at"] = user_tweets["created_at"]/1000
    user_tweets["created_at"] = pd.to_datetime(user_tweets["created_at"], unit='ms')
    #print(user_tweets["D_sentiment"])
    for index, row in user_tweets.iterrows():
         #print(index)
         c_sentiment = row["c_sentiment"]
         D_sentiment = row["D_sentimet"]
         t_target = row["date"]
         t_target = t_target/1000 #convert to unix time stamp format
         t_target = datetime.datetime.utcfromtimestamp(t_target)
         t_target_deltat = t_target - datetime.timedelta(days=time_window)
         #get the history vector : [all_tweets before t_target-delta_t)
         #history = get_history_vector(user_tweets, t_target_deltat)
         #print(history,"history")

         #get the prior vector + multiply with stubbornness socre: all tweets [t_target-delta_t to t_target)
         prior = get_prior_vector(user_tweets, t_target_deltat, t_target)
         if prior !="empty":
           print(prior, "prior")

         #for each freined get the vector [t_target-delta_t to t_target]
         
    # #open json file for each user's friends
    # #get the list of user's friend and their influence score  
    #     friends = user_network_dict[user]
    #     all_friends_Vector = []
    #     for friend in friends:
    #             name = friend[0]
    #             #get the influence score for each user's friends
    #             inf_score = friend[1]

    #             #get the vecor in proper time ([t:t+1) for this fiend (summation)

    #             friend_tweet_data= pd.DataFrame(columns=["tweet_id", "tweet", "opinion_words", "c_centiment", "D_sentiment", "created_at", "date", "time", "vector"])
    #             friend_tweet_file = "./Data/Galaxy_ds/W2Vec/Seed_users_target_tweets/Opinion_word_vec/" + name + ".json"
    #             if os.path.exists(friend_tweet_file) == True:
    #                 with open (friend_tweet_file) as f:
    #                     for line in f:
    #                         data = json.loads(line)
    #                         friend_tweet_data = friend_tweet_data._append(data, ignore_index=True)
    #             #filter friend_tweet_data based on the created_at time
    #             #summation all the vectors and multiply with the influence score
    #             print(friend_tweet_data["vector"])
                
    #             #multiply the influence score with the vector



        
                
                

    #             #call the predictor trainier 

    #             #call predictor tester












