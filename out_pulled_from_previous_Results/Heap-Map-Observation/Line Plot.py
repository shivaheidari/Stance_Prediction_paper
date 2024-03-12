import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

sns.set()
census_data = pd.read_csv('lineplot.csv', delimiter=',', index_col=0)

ax=sns.lineplot(x='Zeta',y='Precision',hue='Type',data=census_data,markers=True)
plt.xlabel("$\zeta$")
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set(xlim=(1,20))

# sns.lmplot('Zeta', 'Precision', data=census_data, hue='Type', ci=None, order=4, truncate=True)
# plt.xlabel("$\zeta$")

# ax = sns.regplot(x='Zeta',y='Precision', data=census_data,order=2, ci=None, truncate=True)
# plt.xlabel("$\zeta$")
ax.axhline(0.5, ls='-.',color='red')
ax.axhline(0.3, ls='--')
ax.axvline(5, ls='--')


plt.show()