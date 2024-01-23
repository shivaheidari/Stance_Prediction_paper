import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from ast import literal_eval
import numpy as np


def load_nd_list(file_name):
    lst = []
    with open(file_name, 'r') as f:
        for line in f:
            lst.append(literal_eval(line))
    return lst


list_hidden = load_nd_list("chart/hidden/report.txt")
list_chen = load_nd_list("chart/chen/report.txt")
chen = pd.DataFrame(list_chen, index=["Accuracy", "F1"])
chen = chen.transpose()


hid = pd.DataFrame(list_hidden, index=["Accuracy", "F1"])
hid = hid.transpose()

sns.set_theme(style="whitegrid")
sns.set_style("darkgrid", {"axes.facecolor": ".9"})
sns.set_context("paper", font_scale=1.4)
sns.kdeplot(x= hid["Accuracy"], label="Proposed model", data = hid)
sns.kdeplot(data=chen["Accuracy"], label="CSIM")
plt.legend()
# plt.savefig("../Out/KDE_acc_CSIM_Proposed")
plt.show()
plt.clf()

# plt.show()
# plt.savefig("../Out/KDE_F1_CSIM_Proposed")

