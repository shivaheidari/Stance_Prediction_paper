# the number of tweets total
import os
import json

users = open("Data/Galaxy_ds/valid_seed_users.txt", 'r')
tweet_per_user = open("Data/Galaxy_ds/tweet_per_user_target.txt", 'w+')

def get_tweets_general(user_file):
    total_tweets = 0
    for user in user_file:
        user_tweets = 0
        user = user.rstrip()
        if os.path.isfile("Data/Galaxy_ds/users_tweets_general/"+user+'.txt') is True:
            
            print(user)
            ufile = open("Data/Galaxy_ds/users_tweets_general/"+user+'.txt', 'r')
            
            for line in ufile:
                total_tweets += 1
                user_tweets += 1
            tweet_per_user.write(user+" "+str(user_tweets)+"\n")
    return total_tweets

def get_tweets_target(user_file):
    total_tweets = 0
    for user in user_file:
        user_tweets = 0
        user = user.rstrip()
        if os.path.isfile("Data/Galaxy_ds/users_target_tweets/"+user+'.txt') is True:
            
            print(user)
            ufile = open("Data/Galaxy_ds/users_target_tweets/"+user+'.txt', 'r')
            
            for line in ufile:
                total_tweets += 1
                user_tweets += 1
            tweet_per_user.write(user+" "+str(user_tweets)+"\n")
    return total_tweets




def get_tweets_sentiment_stats(user_file):
    pos = 0
    neg = 0
    neu = 0

    for user in user_file:
        user = user.rstrip()
        if os.path.isfile("Data/Galaxy_ds/W2Vec/Seed_users_target_tweets/Opinion_word_vec/"+user+'.json') is True:
            ufile = open("Data/Galaxy_ds/W2Vec/Seed_users_target_tweets/Opinion_word_vec/"+user+'.json', 'r')
            for line in ufile:
                #read json file
                line = line.rstrip()
                data = json.loads(line)
                opinion = data.get("D_Sentiment")
                if opinion == 1:
                    pos += 1
                elif opinion == -1:
                    neg += 1    
                else:
                    neu += 1
    return pos, neg, neu



            # for line in ufile:
            #     line = line.rstrip()
            #     if line == 'positive':
            #         pos += 1
            #     elif line == 'negative':
            #         neg += 1
            #     else:
            #         neu += 1


print(get_tweets_sentiment_stats(users))