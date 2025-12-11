import matplotlib.pyplot as plt # PLT - это сокращение от pyplot
x = [1.1, 5.1, 5.1, 1.1, 1.1 ]
y = [1.1, 1.1, 1.5, 1.5, 1.1 ]
plt.plot(x, y, color='g', label='Graf 1', marker='o', ms=5)
plt.savefig("Мой_третий_график.png")