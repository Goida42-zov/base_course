import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import imageio


l, m, n = 1.0, 1.0, 1.0
def f(theta):
    return np.cos(theta)

theta = np.linspace(0, np.pi, 50)
phi = np.linspace(0, 2 * np.pi, 50)
theta, phi = np.meshgrid(theta, phi)

X = phi * np.cos(theta) + l * f(theta)
Y = phi * np.sin(theta) + m * f(theta)
Z = n * f(theta)


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_title('3D Коноид Анимация')
ax.set_xlabel('X'), ax.set_ylabel('Y'), ax.set_zlabel('Z')


def update_plot(frame):
    ax.cla() 
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax.view_init(elev=30, azim=frame * 2)
    ax.set_xlim(X.min(), X.max()), ax.set_ylim(Y.min(), Y.max()), ax.set_zlim(Z.min(), Z.max())
    return fig,

ani = FuncAnimation(fig, update_plot, frames=180, interval=50, blit=True) 


ani.save('conoid_animation.gif', writer='pillow', fps=30)
