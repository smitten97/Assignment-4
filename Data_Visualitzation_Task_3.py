import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname="/Users/jakobsmit/SynologyDrive/PycharmProjects/Programming-for-the-Humanities-E22-main/dat/series-01.csv", delimiter=",")

def groupedPlots():
    fig = plt.figure(figsize=(10, 5))

    for i in range(10):
        axes = fig.add_subplot(2, 5, i+1)
        plt.title(f"Row {i+1}")
        axes.plot(data[i])

    plt.tight_layout()
    plt.savefig("/Users/jakobsmit/SynologyDrive/PycharmProjects/Assignment 4/figs/groupedPlots.png")
    plt.close()

def stackedPlots():
    plt.figure()

    for i in range (8):
        plt.plot(data[i])
        plt.title("Stacked rows")

    plt.tight_layout()
    plt.savefig("/Users/jakobsmit/SynologyDrive/PycharmProjects/Assignment 4/figs/stackedPlots.png")
    plt.close()

if __name__ == "__main__":
    groupedPlots()
    stackedPlots()


