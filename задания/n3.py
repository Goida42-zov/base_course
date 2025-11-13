T = 200
p = 300 # Дж
import numpy as np
from n1 import k, e, h
N = (2 / np.pi ** 0.5) * ((h ** 0.5) * (k * T) ** 1.5 / p * e ** (-p / (k * T)) * p ** T/2)
print(N)