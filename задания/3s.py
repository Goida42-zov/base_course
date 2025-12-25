from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def get_star_coordinates(outer_radius, inner_radius, num_points):
    """Генерирует координаты для правильной звезды."""
    angles = np.linspace(0, 2 * np.pi, 2 * num_points, endpoint=False)
    
    radii = np.tile([outer_radius, inner_radius], num_points)
    x = radii * np.cos(angles)
    y = radii * np.sin(angles)
   
    x = np.append(x, x[0])
    y = np.append(y, y[0])
    return x, y

x, y = get_star_coordinates(outer_radius=20, inner_radius=8, num_points=5)

x0, y0 = 0, 0

fig, ax = plt.subplots(figsize=(7, 7))
star_line, = plt.plot([], [], '-', color='r', label='Звезда', lw=2) # lw - толщина линии

def animate(frame_num):
    # Угол поворота для каждого кадра (полный оборот за 100 кадров)
    alpha = 2 * np.pi * frame_num / 100

    # Применяем матрицу поворота
    X = x * np.cos(alpha) - y * np.sin(alpha)
    Y = x * np.sin(alpha) + y * np.cos(alpha)

    star_line.set_data(X, Y)
    return star_line,

edge = 25 
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ax.set_title('Анимация вращающейся звезды')
ax.grid(True)
ax.legend()

ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=True, repeat=True)
ani.save('rotating_star.gif', writer='pillow', fps=30)
