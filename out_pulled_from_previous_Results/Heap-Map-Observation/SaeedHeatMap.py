import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# data_url = 'http://bit.ly/2cLzoxH'
# gapminder = pd.read_csv(data_url)
# print(gapminder.head(3))
#
# df1 = gapminder[['continent', 'year','lifeExp']]
#
# heatmap1_data = pd.pivot_table(df1, values='lifeExp', index=['continent'], columns='year')
#
# sns.heatmap(heatmap1_data, cmap="YlGnBu")
#
#
# plt.savefig('Co-occurrence-probability-Hour-dimension.png')
# plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.DataFrame(np.random.normal(size=40*40).reshape(40,40))

yticks = data.index
keptticks = yticks[::int(len(yticks)/10)]
yticks = ['' for y in yticks]
yticks[::int(len(yticks)/10)] = keptticks

xticks = data.columns
keptticks = xticks[::int(len(xticks)/10)]
xticks = ['' for y in xticks]
xticks[::int(len(xticks)/10)] = keptticks

sns.heatmap(data,linewidth=0,yticklabels=yticks,xticklabels=xticks)

# This sets the yticks "upright" with 0, as opposed to sideways with 90.
plt.yticks(rotation=0)

plt.show()