import matplotlib.pyplot as plt
import numpy as np

def circle_plotter(radius=10):
    x = np.arange(-2*radius, 2*radius, 0.1)# создание массива значений X от -2R до 2R с шагом 0.1 np.arange - создание массива значений
    y = np.arange(-2*radius, 2*radius, 0.1)# создание массива значений Y от -2R до 2R с шагом 0.1

    # Переход к неявнозаданным координатам
    X, Y = np.meshgrid(x, y)# создание сетки координат из массивов X и Y

    fxy = X**2 + Y**2 - radius**2 # Уравнение окружности x**2 + y ** 2 = R **2 (f(x,y) = 0)

# Команда рисования
    plt.contour(X, Y, fxy, levels=[0])
    plt.axis('equal')                                                   # Равные масштабы по осям X и Y
    
    plt.savefig('функция.png')
    
if __name__ == '__main__':
	circle_plotter()