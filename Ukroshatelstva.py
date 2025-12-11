import matplotlib.pyplot as plt # PLT - это сокращение от pyplot
x = [3, 8, 5]
y = [7, 4, 9]
plt.plot(x, y, color='g', label='Graf 1', marker='>', ms= 5) # label - подпись графика, 
                                                             #marker - маркер (вид точки), 
                                                             #ms - размер маркера
plt.plot(y, x, color='r', label='Graf 2', marker='o', ms= 3)
# ---Украшения графика---
plt.xlabel('курс доллара: ') # подпись оси X
plt.ylabel('курс евро: ') # подпись оси Y
plt.legend('Base') # отображение легенды на графике
plt.title('Мой второй график') # заголовок графика
plt.grid(True) # Подключение сетки         
plt.savefig("Мой_второй_график.png")