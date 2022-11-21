# Assignment 4 - Data Visualitzation
**Imports**

First, we import a few different libraries which are used throughout Assignment 4

```Python 
import numpy as np
import matplotlib.pyplot as plt
```
### 1. Custom Plotting Function and 2. Modify Figure Properties


For the first and second task of Assignment 4, I created a function called "visuaizer" which contains the following code:

```Python
def visualizer(series, filename, plotcolor, plotlinewidth, ylabel, xlabel, title):
    data = np.loadtxt(fname=f"/Users/jakobsmit/SynologyDrive/PycharmProjects/Programming-for-the-Humanities-E22-main/dat/series-{series}.csv" ,delimiter=",")
    ave_value = np.mean(data, axis=0)
    plt.plot(ave_value, color=plotcolor, linewidth=plotlinewidth)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.savefig(f"../Assignment 4/figs/{filename}.png")
    plt.close()
```
The first line of code within the function allows me extract whichever series.csv file I'm interested in which is contained within my /dat file.

The middle part of the code allows me to customize different settings within the plot. Amongst these are options regarding x-and y labels, title of the plots, color of the line in the plot, and the width of the line in the plot. All these are determined once the code is run. 

In the last part of the code, it allows me to save it in my chosen "figs" folder as a .png file with a name that is determined once the code is run.

```Python
visualizer("01", "Series 01 Visualization", "red", 3, "y","x","Title")
visualizer("02", "Series 02 Visualization", "blue", 4,"y","x","Title")
visualizer("03", "Series 03 Visualization", "green", 5,"y","x","Title")
```

Finally the code is fun, where I called 3 different series from the "series".csv files. Likewise, the color, width of the plot, labels and title is also selected. 


### 3. To Stack or not to Stack

First the series-01.csv file is loaded, which is what I have chosen to work with, this is ofcourse totally optional, as I am able to extract whichever series I like.

```Python
data = np.loadtxt(fname="/Users/jakobsmit/SynologyDrive/PycharmProjects/Programming-for-the-Humanities-E22-main/dat/series-01.csv", delimiter=",")
```
Next, a function called "groupedPlots" is defined. 
```Python
def groupedPlots():
    fig = plt.figure(figsize=(10,3))

    for i in range(10):
        axes = fig.add_subplot(2, 5, i+1)
        plt.title(f"Row {i+1}")
        axes.plot(data[i])

    plt.tight_layout()
    plt.savefig("/Users/jakobsmit/SynologyDrive/PycharmProjects/Assignment 4/figs/groupedPlots.png")
    plt.close()
```
This line of code calls for the first 10 lines of numbers in the series-01.csv files, and plots them individually in 2x5 plot. 

Likewise, the title of each plot is determined corresponding with each line it's extracted from. This is done through the "plt.title(f"row {i+1}")

Finally, the file is saved as a .png file under the name "groupedPlots"

```Python
def stackedPlots():
    plt.figure()

    for i in range (8):
        plt.plot(data[i])
        plt.title("Stacked rows")

    plt.tight_layout()
    plt.savefig("/Users/jakobsmit/SynologyDrive/PycharmProjects/Assignment 4/figs/stackedPlots.png")
    plt.close()
```
For the stacked plots, instead of plotting them in each subplot, it takes the first 8 lines of the series-01.csv file and plots them into a single plot. This plot is likewise given a chosen title as "Stacked rows" and saved under the /figs folder as "stackedPlots.png" 

```Python
if __name__ == "__main__":
    groupedPlots()
    stackedPlots()
```

Finally, the two functions are called, saving two different .png files in the /figs folder. 

There is no clear advantage of the grouped plots, hence it's too difficult to differentiate the different plots in the graph. It could be useful if only 2-3 lines were plotted, but since you plot 8 different lines, it's very hard to distinguish and get any meaningful analysis out of the plots. Hence, it's much more advantageous to plot in sub-plots, where you can compare the data more easily.  