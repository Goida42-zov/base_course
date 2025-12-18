import matplotlib.pyplot as plt
import numpy as np

def f(a, b, n):
    x = np.linspace(a, b, n) # linspace - создание массива из n значений от a до b включительно
    plt.ylim(a, b) #lim это границы по оси Y
    plt.plot(x, 1/x)
    plt.savefig('hyperbola.png')

f(-10, 10, 100)
