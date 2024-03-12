from ast import literal_eval
import matplotlib.pyplot as plt

"""--------------------***private_area****--------------------"""


def load_nd_list(file_name):
    lst = []
    with open(file_name, 'r') as f:
        for line in f:
            lst.append(literal_eval(line))
    return lst


def draw_chart(x_tags, y_lists, method_names, filename, title):
    plt.plot()
    markers_lst = ["o", "v", "s", "P", "D", "*", "X", ">"]
    colors_lst = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'tab:orange']

    for i in range(0, len(y_lists)):
        plt.plot(x_tags, y_lists[i], color=colors_lst[i], marker=markers_lst[i], label=method_names[i])

    plt.title(title)

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.01),
               fancybox=True, shadow=True, ncol=4)

    plt.savefig(filename)
    plt.clf()
    plt.cla()
    plt.close()

"""------------------------------------***main_area***---------------------------"""
method_names = ["chen", "hidden"]
f1_y_lists = []
acc_y_lists = []
for method in method_names:
    file_content = load_nd_list("chart/" + method + "/report.txt")
    acc_y_lists.append(file_content[0])
    f1_y_lists.append(file_content[1])

x_tags = [x * 2 for x in range(1, len(acc_y_lists[0]) + 1)]
draw_chart(x_tags, acc_y_lists, method_names, "chart/accuracy.png", "Accuracy ")
draw_chart(x_tags, f1_y_lists, method_names, "chart/f1.png", "F_Measure")
