import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm

#load data train-test
# file = open("Report/Report_train_test_acc.csv", "r")
# df = pd.read_csv(file)
# print(df.head())
# sns.lineplot(x = "Training", y = "Accuracy", data = df, palette="Set2", size=10)
# plt.title('Training and Accuracy Strip Plot')
# plt.xlabel('Training')
# plt.ylabel('Accuracy')
# plt.savefig("Report/Reportline_train_test_acc.png")

#load data csim and HMM
file = open("Report/report_lenght_history.csv", "r")
df = pd.read_csv(file)
print(df.head())
lowess_csim = sm.nonparametric.lowess(df["Accuracy-csim"], df["history"], frac=0.3)
lowess_pp = sm.nonparametric.lowess(df["Accuracy-propose"], df["history"], frac=0.3)
sns.set(style="whitegrid")
sns.lineplot(x =lowess_csim[:,0], y = lowess_csim[:,1], label="CSIM", ci=None)
sns.lineplot(x =lowess_pp[:,0], y = lowess_pp[:,1], label="proposed model", ci=None)
#sns.lineplot(x = "history", y = "Accuracy-propose", data = df, marker = "o", label="Proposed Model", ci=None)
plt.title('Length vs Accuracy')
plt.xlabel('Length')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig("Report/report_lenght_history_smooth.png")