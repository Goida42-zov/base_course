import numpy as np

h = 100
a = 45
b = 35

from n1 import g

v = g * h * np.tan(b) ** 2 / (2 * np.cos(a) ** 2) * (1 - np.tan(b) / np.tan(a)) ** 0.5

print(v)


