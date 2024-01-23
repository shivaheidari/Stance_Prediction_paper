import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

db_confing = {"host": "localhost",
              "user": "root",
                "password": "root",
                "database": "oprediction"}

connection = mysql.connector.connect(**db_confing)


query = "select * from tweets_target"
df = pd.read_sql(query, connection)
connection.close()


#histogram of D_sentiment values
# plt.figure(figsize=(10,10))
# plt.hist(df["D_sentiment"], bins=3, color="blue", edgecolor="black")
# plt.title("Distribution of D_sentiment values")
# plt.xlabel("D_sentiment")
# plt.ylabel("Number of tweets")
sns.set_style("whitegrid")
ax = sns.histplot(data=df["D_sentiment"], bins=3, color="lightblue", edgecolor="black")
plt.savefig("histogram_D_sentiment_sns.png")