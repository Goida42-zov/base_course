import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


t_values = np.linspace(0, 4 * np.pi, 200)
x_base = 12 * np.cos(t_values) + 8 * np.cos(1.5 * t_values)
y_base = 12 * np.sin(t_values) + 8 * np.sin(1.5 * t_values)

fig, ax = plt.subplots(figsize=(7, 7))
star_line, = ax.plot([], [], '-', color='r', lw=2, label='Вращающаяся звезда')


edge = 25 
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_title('Анимация вращающейся звезды')
ax.legend()

def animate(frame_num):
   
    alpha = 2 * np.pi * frame_num / 100 
    
   
    X = x_base * np.cos(alpha) - y_base * np.sin(alpha)
    Y = x_base * np.sin(alpha) + y_base * np.cos(alpha)

    star_line.set_data(X, Y)
    return star_line,


ani = FuncAnimation(fig, animate, frames=100, interval=30, blit=True, repeat=True)

plt.show()

ani.save('rotating_star.gif', writer='pillow', fps=30)
