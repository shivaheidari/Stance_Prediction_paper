import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

sns.set()
census_data = pd.read_csv('lineplot.csv', delimiter=',', index_col=0)


ax=sns.scatterplot(x='Zeta',y='Precision',hue='Type',data=census_data)
plt.xlabel("$\zeta$")
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
# ax.set(xlim=(1,20))

ax.axhline(0.5, ls='--',color='red')
ax.axhline(0.3, ls='--')
ax.axvline(5, ls='--')

ax.text(0.5,5, "Some text")
ax.text(0.3,5, "Some text")


plt.show()
