import mysql.connector
import pandas as pd
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
#number of users with unique tweets
#time queirs


query = "select username , max(ddate) as last, min(ddate) as first, DATEDIFF(max(ddate), min(ddate)) as delta_t_in_days from tweets_target group by username;"
cursor.execute(query)
res = cursor.fetchall()
result = pd.DataFrame(res, columns=["username", "last", "first", "delta_t_in_days"])
result = result[result["delta_t_in_days"]>=7]
print(result.shape)
result.to_csv("Data/Galaxy_ds/seed_users_active.csv", index=False)
#print(result)
#result.to_csv("Data/Galaxy_ds/users_delta_t.csv", index=False)

#usernames = pd.DataFrame(usernames, columns=["username", "count"])
#usernames.to_csv("Data/Galaxy_ds/users_unique_tweets.csv", index=False)

