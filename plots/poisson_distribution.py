import pandas as pd
import numpy as np
import scipy.stats as stats
from sqlalchemy import create_engine
from sqlalchemy import URL
from sqlalchemy import text
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

engine = create_engine("mysql+pymysql://root:root@localhost:3306/oprediction")




#count the number of tweets per person
with engine.connect() as con:
    query = text("SELECT username, count(*) FROM tweets_target GROUP BY username")
    result = con.execute(query)
    data = result.fetchall()
    data = pd.DataFrame(data, columns=['username', 'count'])

data["username_encoded"] = pd.Categorical(data["username"]).codes


x = sm.add_constant(data["username_encoded"])
y = data["count"]

model = sm.GLM(y, x, family=sm.families.Poisson()).fit()

data["predicted"] = model.predict(x)

sns.set_theme(style="whitegrid")
sns.scatterplot(x= 'username_encoded', y='count', data=data, label='Actual')
sns.lineplot(x= 'username_encoded', y='predicted', data=data, label='Predicted')
plt.xlabel('users')
plt.ylabel('number of tweets')

plt.legend()
plt.show()
plt.savefig('plots/poisson_distribution.png')
