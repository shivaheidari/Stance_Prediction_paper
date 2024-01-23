# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:46:57 2019

@author: Saeid
"""

import pandas as pd
import seaborn as sns; sns.set()
from matplotlib import pyplot as plt
import scipy as sc 
import numpy as np


# #Heatmap original
#
# flights_long = sns.load_dataset("flights")
# flights = flights_long.pivot("month", "year", "passengers")
#
# #print(flights)
#
# f, ax = plt.subplots(figsize=(9, 6))
# sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax)


#custom heatmap 01
#flights_long = pd.read_csv('avocado.csv')
#flights = flights_long.pivot("year", "region", "AveragePrice")
#
##print(flights)
#
#f, ax = plt.subplots(figsize=(9, 6))
##sns.heatmap(flights, annot=True, fmt="d",linewidths=.5, ax=ax)
#sns.heatmap(flights, annot=True,linewidths=.5, ax=ax)

#custom heatmap 02

f_long = pd.read_csv('dayHour.csv')

f1 = f_long.pivot("[word pair co-occurrence]", "[hour period]", "probablity")

# mask = np.zeros_like(f1)
# mask[np.triu_indices_from(mask)] = True

f, ax = plt.subplots(figsize=(9, 6))
sns.set(font_scale=1.3)
sns.axes_style()
hours=sns.heatmap(f1, annot=True,linewidths=.5, ax=ax, square=True,annot_kws={"size": 20})

sns.axes_style({'axes.axisbelow': True,
 'axes.edgecolor': '.8',
 'axes.facecolor': 'whi'})

for item in hours.get_yticklabels():
    item.set_rotation(360)

plt.xlabel('Hourly period',size=20)
plt.ylabel('Probability',size=20)

plt.savefig('Co-occurrence-probability-Hour-dimension.png')
plt.show()

# Co-occurrence probability Season dimension
f_long = pd.read_csv('season.csv')

f1 = f_long.pivot("[word pair co-occurrence]", "[annual season]", "probablity")

f, ax = plt.subplots(figsize=(9, 6))

ax.set_ymargin(0.1)
sns.set(font_scale=1.3)
season=sns.heatmap(f1, annot=True,linewidths=.5, ax=ax, square=True,annot_kws={"size": 20})

for item in season.get_yticklabels():
    item.set_rotation(360)

plt.xlabel('Season',size=20)
plt.ylabel('Probability',size=20)


plt.savefig('Co-occurrence-probability-season-dimension.png')
plt.show()



