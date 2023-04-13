import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from ast import literal_eval


# load data

def load_nd_list(file_name):
    lst = []
    with open(file_name, 'r') as f:
        for line in f:
            lst.append(literal_eval(line))
    return lst


list_hidden = load_nd_list("chart/hidden/report.txt")
list_chen = load_nd_list("chart/chen/report.txt")


