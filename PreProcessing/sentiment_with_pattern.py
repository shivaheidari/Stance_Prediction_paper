# -*- coding: utf-8 -*-
"""Sentiment with pattern.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oGUbVf032ut1BxUNlsp_KdB6jXug30ki
"""

# !pip3 install pattern

import pattern
import pandas as pd
from pattern.en import sentiment
import codecs
import json


source = "/content/drive/My Drive/Data/users_target_tweets"
dest = "/content/drive/My Drive/Data/Preprocess_subj_stance"

def give_source(uname):
  return source + '/'+ uname+'.txt'

def give_dest(uname):
  return dest + '/'+ uname+'.txt'
  
def sentiment_oriented(tweet_txt):
    return sentiment(tweet_txt)[0]

def sentiment_oriented_subj(tweet_txt):
    return sentiment(tweet_txt)[1]

users = open("/content/drive/My Drive/Data/valid_seed_users.txt",'r')
for user in users:
  json_tweets = []
  user = user.rstrip()
  des = give_dest(user)
  tweet_file = pd.read_json(codecs.open(give_source(user), 'r', 'utf-8'), orient='records', lines=True)
  tweet_file["sentiment_orientation"] = tweet_file["tweet"].apply(lambda x: sentiment_oriented(x))
  tweet_file["sentiment_subj"] = tweet_file["tweet"].apply(lambda x: sentiment_oriented_subj(x))
  #json_tweets.append({"tweet_id":str(tweet_file["id"]),"created_at":tweet_file["created_at"],  })
  for idx in tweet_file.index:
        l = 0
        dl = 0
        tweet_text = tweet_file.at[idx, 'tweet']
        
        # pre_obj = cleaning_text(tweet_text)
        # pre_obj.lower()
        # pre_obj.punctuation()
        # pre_obj.tokenizing()
        # pre_obj.stopword()
        # pre_obj.stemming()
        # tokens = getattr(pre_obj, 'tokenized')

        json_tweets.append({'tweet_id': str(tweet_file.at[idx, 'id']), 'tweet': tweet_text,
                            'sentiment_orientation': tweet_file.at[idx, "sentiment_orientation"], 'sentiment_subj': tweet_file.at[idx, "sentiment_subj"],
                             'created_at': str(tweet_file.at[idx, 'created_at']),
                            'date': str(tweet_file.at[idx, 'date']), 'time': str(tweet_file.at[idx, 'time'])})

        
        with codecs.open(des, 'a+', 'utf-8') as fp:
               for jsl in json_tweets:
                fp.write(json.dumps(jsl, ensure_ascii=False))
                fp.write("\n")



