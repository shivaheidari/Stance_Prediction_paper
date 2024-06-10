import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

db_confing = {
    'host': 'localhost',
    "user": "root",
    "password": "root",
    "database": "oprediction"
}

connection = mysql.connector.connect(**db_confing)
if connection.is_connected():
    print("connected")

cursor = connection.cursor()

#load in dataframe 
query = "select * from tweets_target"
df = pd.read_sql(query, connection)
connection.close()


#cut based on the number of tweets 
bins_tweet_number = [0,3,5,8,10,15,20]


tweets_per_user= df["username"].value_counts().reset_index()

tweets_per_user.columns = ["username", "tweet_count"]

df = pd.merge(df, tweets_per_user, on="username", how="left")
df["bin_tweet_nums"] = pd.cut(df["tweet_count"], bins=bins_tweet_number, labels=[1,2,3,4,5,6])
#plot

plt.figure(figsize=(10,10))
plt.hist(df["bin_tweet_nums"], bins=bins_tweet_number, color="blue", edgecolor="black")
plt.title("Number of users per bin")
plt.xlabel("Number of tweets")
plt.ylabel("Number of users")
plt.xticks(bins_tweet_number)
plt.savefig("histogram_tweets.png")

