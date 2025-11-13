import numpy as np
a = [1, 5, 3, 6]
slise = a[0:2:1]
print(slise)

slise = a[3:0: -1]
print(slise)

slise = a[ : : -1]
print(slise)

b = np.array([a, np.array(a) * 3])
print(b)

slice = b[::, 1] # с нулевой по первую строчку с шагом один, первй столбец
print(slice)
