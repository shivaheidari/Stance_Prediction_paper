import pandas as pd
import mysql.connector

db_confing = {"host": "localhost",
              "user": "root",
              "password": "root",
                "database": "oprediction"}

connection = mysql.connector.connect(**db_confing)
if connection.is_connected():
    print("connected")


query = "select username from tweets_target where D_sentiment in (-1,0,1) group by username having Count(Distinct D_sentiment)=3 and Count(*)>=40;"
cursor = connection.cursor()
cursor.execute(query)
res = cursor.fetchall()
print(res.__len__())
Sampled_users = pd.DataFrame(res, columns=["username"])
print(Sampled_users.shape)
#print(Sampled_users.head(30))
Sampled_users.to_csv("Data/Galaxy_ds/Sampled_users_40.csv", index=False)

