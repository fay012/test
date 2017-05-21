#https://matplotlib.org/examples/pylab_examples/boxplot_demo.html

import matplotlib.pyplot as plt
from pylab import *

def line_plot(x, y, x_name, y_name):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #ax.set_title(title)
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    ax.plot(x,y)
    plt.show()

def box_plot(y,y_name):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.boxplot(y)
    ax.set_ylabel(y_name)
    plt.show()

def hist_plot(x,x_name):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(x)
    ax.set_xlabel(x_name)
    plt.show()

def scatter_plot(x,y,x_name,y_name):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # ax.set_title(title)
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    ax.scatter(x, y)
    plt.show()

if __name__ == '__main__':
    y = [1.11,2,3]
    hist_plot(y,'y')





