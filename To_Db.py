#transfer all the tweets to sqlite db from csv files
import mysql.connector
import json
import datetime
import pymysql

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



# queries = ["use oprediction;","create table tweets_target(username varchar(255), tweet_id varchar(255), tweet varchar(800), opinion_words Text, c_sentiment int, D_sentiment float, created_at datetime, date datetime, vector Text );"]
# for query in queries:
#     cursor.execute(f'{query}')
#     print("executed")




usernames = open("Data/Galaxy_ds/valid_seed_users_v2.txt", "r")
usernames = usernames.readlines()
usernames = [x.strip() for x in usernames]

for username in usernames:
        print(username)
        user_file = "Data/Galaxy_ds/W2Vec/Seed_users_target_tweets/Opinion_word_vec/"+username + ".json"
        with open (user_file, "r") as file:
            for line in file:
                
                    tweets = json.loads(line)
                    
                    opinion_words = tweets.get("opinion_words")
                    if opinion_words:
                        opinion_words = json.dumps(tweets["opinion_words"])
                    else:
                            opinion_words = "[]"
                    
                    vector = json.dumps(tweets["vector"])
                    timestamp = tweets["created_at"]
                    timestamp_seconds = timestamp/1000.0
                    date = datetime.datetime.utcfromtimestamp(timestamp_seconds)
                    formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
                    date_only = tweets["date"]
                    date_only = date_only/1000.0
                    date = datetime.datetime.utcfromtimestamp(date_only)
                    form_date = date.strftime('%Y-%m-%d %H:%M:%S')
                    query = "insert into tweets_target (username, tweet_id, tweet, opinion_words, c_sentiment, D_sentiment, created_at, date, vector) values( %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(query, (username, tweets["tweet_id"], tweets["tweet"], opinion_words, tweets["c_sentiment"], tweets["D_sentimet"], formatted_date, form_date, vector))
                    #cursor.execute(f"insert into tweets_target (username, tweet_id, tweet, opinion_words, c_sentiment, D_sentiment, created_at, date, vector) values ('{username}', '{tweets['tweet_id']}', '{tweets['tweet']}', '{opinion_words}', '{tweets['c_sentiment']}', '{tweets['D_sentimet']}', '{formatted_date}', '{form_date}', '{vector}');")
                    connection.commit()

                






