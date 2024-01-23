#one line display the plot - Simple smoothed line plot

#from scipy.interpolate import interp1d
#from scipy.optimize import fmin
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#
#df=pd.read_csv("KMedoid.txt",delimiter = ',')
#  
#x = df['zeta']
#y = df['Score']
#
#f = interp1d(x, y, kind='cubic', bounds_error=False, fill_value='extrapolate')
#
#xfit = np.linspace(1,50)
#
#plt.plot(x,y,'bo')
#plt.plot(xfit, f(xfit),'r-')
#
#plt.legend(['data','fit','max'], loc='best', numpoints=1)
#plt.xlabel('x data')
#plt.ylabel('y data')
#
#plt.savefig('splinefit.png')
#plt.show()
###############################################################################
import pandas as pd
import seaborn as sns; sns.set()
from matplotlib import pyplot as plt
import scipy as sc 
import numpy as np

sns.set_style("whitegrid")
########################################### K-Medoid Clustering
df0=pd.read_csv("KMedoid.txt")

#K==20
df=df0.query("Clusters == '20'")

x = df['zeta']
y = df['Score']
z= df['Clusters']

f = sc.interpolate.interp1d(x, y, kind='cubic', bounds_error=False, fill_value='extrapolate')

xfit = np.linspace(1,50)

sns.lineplot(x=x,y=y,color=[0.55, 0.76, 0.98])
sns.lineplot(x=xfit, y=f(xfit),color=[0.25, 0.5, 0.73], label="k = 20")

#plt.show()

#K==22
df=df0.query("Clusters == '22'")

x = df['zeta']
y = df['Score']
z= df['Clusters']

f = sc.interpolate.interp1d(x, y, kind='cubic', bounds_error=False, fill_value='extrapolate')

xfit = np.linspace(1,50)

sns.lineplot(x=x,y=y,color=[1.0, 0.69, 0.39])
sns.lineplot(x=xfit, y=f(xfit),color=[0.82, 0.49, 0.19], label="k = 22")

#K==24
df=df0.query("Clusters == '24'")

x = df['zeta']
y = df['Score']
z= df['Clusters']

f = sc.interpolate.interp1d(x, y, kind='cubic', bounds_error=False, fill_value='extrapolate')

xfit = np.linspace(1,50)

sns.lineplot(x=x,y=y,color=[0.56, 0.56, 0.56])
sns.lineplot(x=xfit, y=f(xfit),color=[0.24, 0.24, 0.24], label="k = 24")

#K==24
df=df0.query("Clusters == '26'")

x = df['zeta']
y = df['Score']
z= df['Clusters']

f = sc.interpolate.interp1d(x, y, kind='cubic', bounds_error=False, fill_value='extrapolate')

xfit = np.linspace(1,50)

sns.lineplot(x=x,y=y,color=[1.0, 0.85, 0.1])
sns.lineplot(x=xfit, y=f(xfit),color=[0.9, 0.65, 0], label="k = 26")

plt.xlabel('$\zeta$')
plt.ylabel('Accuracy')

plt.savefig('kmeans-k.png')
plt.show()

########################################### DBSCAN Clustering
df0=pd.read_csv("DBScan.txt")

#\epsilon==0.36
df=df0.query("Eps == '0.36'")

x = df['zeta']
y = df['Score']
z= df['Eps']

f = sc.interpolate.interp1d(x, y, kind='cubic', bounds_error=False, fill_value='extrapolate')

xfit = np.linspace(1,50)

sns.lineplot(x=x,y=y,color=[0.55, 0.76, 0.98])
sns.lineplot(x=xfit, y=f(xfit),color=[0.25, 0.5, 0.73], label="$\epsilon$ = 0.36")

#plt.show()

#Eps==0.38
df=df0.query("Eps == '0.38'")

x = df['zeta']
y = df['Score']
z= df['Eps']

f = sc.interpolate.interp1d(x, y, kind='cubic', bounds_error=False, fill_value='extrapolate')

xfit = np.linspace(1,50)

sns.lineplot(x=x,y=y,color=[1.0, 0.69, 0.39])
sns.lineplot(x=xfit, y=f(xfit),color=[0.82, 0.49, 0.19], label="$\epsilon$ = 0.38")

#Eps==0.4
df=df0.query("Eps == '0.4'")

x = df['zeta']
y = df['Score']
z= df['Eps']

f = sc.interpolate.interp1d(x, y, kind='cubic', bounds_error=False, fill_value='extrapolate')

xfit = np.linspace(1,50)

sns.lineplot(x=x,y=y,color=[0.56, 0.56, 0.56])
sns.lineplot(x=xfit, y=f(xfit),color=[0.24, 0.24, 0.24], label="$\epsilon$ = 0.4")

#Eps==0.42
df=df0.query("Eps == '0.42'")

x = df['zeta']
y = df['Score']
z= df['Eps']

f = sc.interpolate.interp1d(x, y, kind='cubic', bounds_error=False, fill_value='extrapolate')

xfit = np.linspace(1,50)

sns.lineplot(x=x,y=y,color=[1.0, 0.85, 0.1])
sns.lineplot(x=xfit, y=f(xfit),color=[0.9, 0.65, 0], label="$\epsilon$ = 0.42")

plt.xlabel('$\zeta$')
plt.ylabel('Accuracy')

plt.savefig('DB-Scan.png')
plt.show()