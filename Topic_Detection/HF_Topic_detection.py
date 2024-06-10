
# print(torch.rand(5, 3))
# from transformers import pipeline
# print(pipeline('sentiment-analysis')('we love you'))

import os
from transformers import AutoModelForSequenceClassification, TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import expit


class topic_prediction():
    def __init__(self, tweet):
        self.tweet = tweet
    def predict(self):
        MODEL = f"cardiffnlp/tweet-topic-21-multi"
        tokenizer = AutoTokenizer.from_pretrained(MODEL)
        model = AutoModelForSequenceClassification.from_pretrained(MODEL)
        class_mapping = model.config.id2label
        tweet = self.tweet
        tokens = tokenizer(tweet, return_tensors='pt')
        output = model(**tokens)
        scores = output[0][0].detach().numpy()
        scores = expit(scores)
        predictions = (scores >= 0.7) * 1
        for i in range(len(predictions)):
            if predictions[i]:
                return class_mapping[i]
        return "None"


#general tweets topic detection
#for each user its important to detect at most 10 topics

source = "Data/Galaxy_ds/Topic_Detection/cleaned_Tweets_seeds_general"
destination = "Data/Galaxy_ds/Topic_Detection/seed_users_topics"

user_list = open("Data/Galaxy_ds/valid_seed_users.txt", 'r')



limitation = 50 #maximum number of topics for each user
processed_count = 0

for uname in user_list:
    print(uname)
    processed_count += 1
    print(processed_count, uname)
    uname = uname.rstrip()
    tweets = open(source + "/" + uname+".txt", 'r')
    #check if the tweets file is exist
    if not os.path.exists(destination + "/" + uname+".txt"):
        
        topics ={}
        counter = 0
        for tweet in tweets:
            if counter < limitation:
                    counter += 1
                    topic = topic_prediction(tweet).predict()
                    if topic != "None":
                        if topic in topics:
                            topics[topic] += 1
                        else:
                            topics[topic] = 1
        for topic in topics:
            with open(destination + "/" + uname+".txt", 'a+', encoding='utf-8') as file:
                file.write(topic + " " + str(topics[topic]) + "\n")

