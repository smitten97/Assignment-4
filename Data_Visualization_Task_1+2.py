import numpy as np
import matplotlib.pyplot as plt

def visualizer(series, filename, plotcolor, plotlinewidth, ylabel, xlabel, title):
    data = np.loadtxt(fname=f"/Users/jakobsmit/SynologyDrive/PycharmProjects/Programming-for-the-Humanities-E22-main/dat/series-{series}.csv" ,delimiter=",")
    ave_value = np.mean(data, axis=0)
    plt.plot(ave_value, color=plotcolor, linewidth=plotlinewidth)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.savefig(f"../Assignment 4/figs/{filename}.png")
    plt.close()

visualizer("01", "Series 01 Visualization", "red", 3, "y","x","Title_example_1")
visualizer("02", "Series 02 Visualization", "blue", 4,"y","x","Title_example_2")
visualizer("03", "Series 03 Visualization", "green", 5,"y","x","Title_example_3")



