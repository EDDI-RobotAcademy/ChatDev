# graphing.py
'''
Graphing File
'''
import matplotlib.pyplot as plt
def plot_function(func, x_range):
    x = []
    y = []
    for i in range(x_range[0], x_range[1] + 1):
        x.append(i)
        y.append(func(i))
    plt.plot(x, y)
    plt.show()