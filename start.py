
# print(torch.rand(5, 3))
# from transformers import pipeline
# print(pipeline('sentiment-analysis')('we love you'))
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
    
