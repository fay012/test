#https://matplotlib.org/examples/pylab_examples/boxplot_demo.html

import matplotlib.pyplot as plt

def line_plot(x, y, x_name, y_name, title):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    ax.plot(x,y)
    plt.show()






