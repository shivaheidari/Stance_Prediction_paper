import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
# sns.set()



# Scores+3

# census_data = pd.read_csv('Scores+3.csv', delimiter=',', index_col=0)
# ax=sns.lineplot(x='Zeta',y='Precision',hue='Type',style="Type", markers=True,data=census_data)
# ax.xaxis.set_major_locator(MaxNLocator(integer=True))
# plt.xlabel("$\zeta$")
# plt.ylabel("Precision")
# ax.set(ylim=(0,0.8))
# ax.set(xlim=(0,20.5))
# ax.grid(True)
# ax.xaxis.grid()
# plt.savefig('Scores+3', dpi=None, facecolor='w', edgecolor='w',
#         orientation='portrait', papertype=None, format=None,
#         transparent=False, bbox_inches=None, pad_inches=0.1,
#         frameon=None, metadata=None)






# Scores-3

# census_data = pd.read_csv('Scores-3.csv', delimiter=',', index_col=0)
# ax=sns.lineplot(x='Zeta',y='Precision',hue='Type',style="Type", markers=True,data=census_data)
# ax.xaxis.set_major_locator(MaxNLocator(integer=True))
# plt.xlabel("$\zeta$")
# plt.ylabel("Precision")
# ax.set(ylim=(0,0.8))
# ax.set(xlim=(0,20.5))
# ax.grid(True)
# ax.xaxis.grid()
# plt.savefig('Scores-3', dpi=None, facecolor='w', edgecolor='w',
#         orientation='portrait', papertype=None, format=None,
#         transparent=False, bbox_inches=None, pad_inches=0.1,
#         frameon=None, metadata=None)







# Scores+3Modified

# census_data = pd.read_csv('Scores+3Modified.csv', delimiter=',', index_col=0)
# ax=sns.lineplot(x='Zeta',y='Precision',hue='Type',style="Type", markers=True,data=census_data)
# ax.xaxis.set_major_locator(MaxNLocator(integer=True))
# plt.xlabel("$\zeta$")
# plt.ylabel("Precision")
# ax.set(ylim=(0,0.7))
# ax.set(xlim=(0,20.5))
# ax.grid(True)
# ax.xaxis.grid()
# plt.savefig('Scores+3Modified', dpi=None, facecolor='w', edgecolor='w',
#         orientation='portrait', papertype=None, format=None,
#         transparent=False, bbox_inches=None, pad_inches=0.1,
#         frameon=None, metadata=None)






# Scores-3Modified

# census_data = pd.read_csv('Scores-3Modified.csv', delimiter=',', index_col=0)
# ax=sns.lineplot(x='Zeta',y='Precision',hue='Type',style="Type", markers=True,data=census_data)
# ax.xaxis.set_major_locator(MaxNLocator(integer=True))
# plt.xlabel("$\zeta$")
# plt.ylabel("Precision")
# ax.set(ylim=(0,0.7))
# ax.set(xlim=(0,20.5))
# ax.grid(True)
# ax.xaxis.grid()
# plt.savefig('Scores-3Modified', dpi=None, facecolor='w', edgecolor='w',
#         orientation='portrait', papertype=None, format=None,
#         transparent=False, bbox_inches=None, pad_inches=0.1,
#         frameon=None, metadata=None)






# Regplot Sample

# census_data = pd.read_csv('Scores+3.csv', delimiter=',', index_col=0)
# ax = sns.regplot(x='Zeta',y='Precision', data=census_data,order=2, ci=None, truncate=True)
# plt.xlabel("$\zeta$")
# plt.ylabel("Precision")
# ax.grid(True)
# ax.xaxis.grid()
# plt.savefig('Regplot', dpi=None, facecolor='w', edgecolor='w',
#         orientation='portrait', papertype=None, format=None,
#         transparent=False, bbox_inches=None, pad_inches=0.1,
#         frameon=None, metadata=None)






# ClusterNumbereffect

# census_data = pd.read_csv('ClusterNumbereffect.csv', delimiter=',', index_col=0)
# ax=sns.lineplot(x='Zeta',y='Precision',hue='Type',style="Type", markers=True,data=census_data)
# ax.xaxis.set_major_locator(MaxNLocator(integer=True))
# plt.xlabel("$\zeta$")
# plt.ylabel("Precision")
# ax.set(ylim=(0,0.18))
# ax.set(xlim=(0,22.5))
# ax.grid(True)
# ax.xaxis.grid()
# plt.savefig('ClusterNumbereffect', dpi=None, facecolor='w', edgecolor='w',
#         orientation='portrait', papertype=None, format=None,
#         transparent=False, bbox_inches=None, pad_inches=0.1,
#         frameon=None, metadata=None)






# ConceptVectorImpact

# census_data = pd.read_csv('ConceptVectorImpact.csv', delimiter=',', index_col=0)
# ax=sns.lineplot(x='Zeta',y='Precision',hue='Type',style="Type", markers=True,data=census_data)
# ax.axvline(0, ls='--')
# ax.axvline(1, ls='--')
# ax.axvline(0.6, ls='--')
# ax.text(1.01,0.5,'Concept only',rotation=90,fontsize=13)
# ax.text(-0.04,0.5,'Content only',rotation=90,fontsize=13)
# ax.text(0.61,0.55,'Best combination',rotation=90,fontsize=13)
# ax.set(xlim=(-0.05,1.05))
# ax.set(ylim=(0,0.95))
# plt.ylabel("Precision")
# ax.grid(True)
# ax.set_xlabel("Concept vector impact ratio",fontsize=16)
# ax.set_ylabel("Precision",fontsize=16)
# ax.tick_params(labelsize=12)
#
# plt.setp(ax.get_legend().get_texts(), fontsize='14')
# ax.xaxis.grid()
# plt.xlabel("Concept vector impact ratio")
# plt.savefig('ConceptVectorImpact', dpi=None, facecolor='w', edgecolor='w',
#         orientation='portrait', papertype=None, format=None,
#         transparent=False, bbox_inches=None, pad_inches=0.1,
#         frameon=None, metadata=None)







# EPS_Clusters

# census_data = pd.read_csv('EPS_Clusters.csv', delimiter=',', index_col=0)
# ax=sns.scatterplot(x='Zeta',y='Clusters', markers=True,data=census_data)
# ax.axvline(0.325, ls='--',color='red')
# ax.axvline(0.475, ls='--',color='red')
# ax.set(xlim=(0,1.2))
# ax.set(ylim=(0,40))
# plt.xlabel("$\epsilon$")
# plt.ylabel("Number of clusters")
# ax.grid(True)
# ax.set_xlabel("$\epsilon$",fontsize=19)
# ax.set_ylabel("Number of clusters",fontsize=18)
# ax.tick_params(labelsize=14)
#
# # plt.setp(ax.get_legend().get_texts(), fontsize='14')
# ax.xaxis.grid()
# plt.savefig('EPS_Clusters', dpi=None, facecolor='w', edgecolor='w',
#         orientation='portrait', papertype=None, format=None,
#         transparent=False, bbox_inches=None, pad_inches=0.1,
#         frameon=None, metadata=None)






# K_Medoid_Cluster_Score

census_data = pd.read_csv('K_Medoid_Cluster_Score.csv', delimiter=',', index_col=0)
ax=sns.scatterplot(x='Clusters',y='Score',hue='Type',style="Type", markers=True,data=census_data)
plt.xlabel("Number of clusters")
plt.ylabel("Score")
ax.axvline(15, ls='--',color='red')
ax.axvline(30, ls='--',color='red')
ax.set(xlim=(0,135))
ax.set(ylim=(0,2))
ax.grid(True)
ax.set_xlabel("Number of clusters",fontsize=19)
ax.set_ylabel("Score",fontsize=18)
ax.tick_params(labelsize=13)
ax.xaxis.grid()
plt.savefig('K_Medoid_Cluster_Score', dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)







# K_Medoid_InnerSimilarity

# census_data = pd.read_csv('K_Medoid_InnerSimilarity.csv', delimiter=',', index_col=0)
# ax=sns.scatterplot(x='Clusters',y='Score', markers=True,data=census_data)
# ax.axvline(15, ls='--',color='red')
# ax.axvline(30, ls='--',color='red')
# ax.set(xlim=(0,135))
# ax.set(ylim=(0,27))
# plt.xlabel("Number of clusters")
# plt.ylabel("Inner similarity score (X1000)")
# ax.grid(True)
# ax.xaxis.grid()
# plt.savefig('K_Medoid_InnerSimilarity', dpi=None, facecolor='w', edgecolor='w',
#         orientation='portrait', papertype=None, format=None,
#         transparent=False, bbox_inches=None, pad_inches=0.1,
#         frameon=None, metadata=None)







# Siloh_Davis_Clusters

# census_data = pd.read_csv('Siloh_Davis_Clusters.csv', delimiter=',', index_col=0)
# ax=sns.scatterplot(x='Clusters',y='Score',hue='Type',style="Type", markers=True,data=census_data)
# plt.xlabel("Number of clusters")
# plt.ylabel("Score")
# ax.set(ylim=(-0.5,1.5))
# ax.set(xlim=(0,40))
# ax.grid(True)
# ax.xaxis.grid()
# ax.axvline(15, ls='--',color='red')
# plt.savefig('Siloh_Davis_Clusters', dpi=None, facecolor='w', edgecolor='w',
#         orientation='portrait', papertype=None, format=None,
#         transparent=False, bbox_inches=None, pad_inches=0.1,
#         frameon=None, metadata=None)







# Siloh_Davis_Eps

# census_data = pd.read_csv('Siloh_Davis_Eps.csv', delimiter=',', index_col=0)
# ax=sns.scatterplot(x='Epsilon',y='Score',hue='Type',style="Type", markers=True,data=census_data)
# plt.xlabel("$\epsilon$")
# plt.ylabel("Score")
# ax.set(ylim=(-0.5,1.5))
# ax.set(xlim=(0,0.71))
# ax.grid(True)
# ax.set_xlabel("$\epsilon$",fontsize=19)
# ax.set_ylabel("Score",fontsize=16)
# ax.tick_params(labelsize=10.5)
# ax.xaxis.grid()
# ax.axvline(0.325, ls='--',color='red')
# ax.axvline(0.4, ls='--',color='green')
# ax.axvline(0.475, ls='--',color='red')
# plt.savefig('Siloh_Davis_Eps', dpi=None, facecolor='w', edgecolor='w',
#         orientation='portrait', papertype=None, format=None,
#         transparent=False, bbox_inches=None, pad_inches=0.1,
#         frameon=None, metadata=None)
