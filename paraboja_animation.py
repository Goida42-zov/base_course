import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation # Это класс для создания анимаций

# Создание пространства для анимации
fig, ax = plt.subplots() # Создаем фигуру и оси для анимации
anim_object, = plt.plot([],[], "-", lw=2) # Линия, которая будет анимироваться [] [] - начальные данные(он перебирает их)
x, y = [],[] # Пустые списки для хранения координат
frames_interval =np.linspace(0, 2*np.pi, 100) # Создаем массив из 100 точек от 0 до 2π
ax.set_xlim(0, 2*np.pi) # Устанавливаем пределы по оси x
ax.set_ylim(-1, 1) # Устанавливаем пределы


def update(frame):
    x.append(frame) # расчёт координаты X
    y.append(np.sin(frame)) # расчёт координаты Y
    anim_object.set_data(x, y) # передача координат объекту анимации
    return anim_object, # Возвращаем обновленный объект анимации

ani = FuncAnimation(fig, 
                    update,
                      frames=frames_interval,
                      interval=50) # frames - кадры анимации, interval - задержка между кадрами в миллисекунда х
ani.save('sine_wave_animation.gif', writer='pillow') # Сохраняем анимацию в файл формата gif
