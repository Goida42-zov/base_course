import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle


a = 0.5  
T_MAX = 20.0 
NUM_FRAMES = 200 

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-(a * T_MAX + 1), (a * T_MAX + 1))
ax.set_ylim(-(a * T_MAX + 1), (a * T_MAX + 1))
ax.set_aspect('equal')
ax.set_title(f'Анимация расширяющегося круга (r(t) = {a}*t)')
ax.grid(True, linestyle='--', alpha=0.6)

circle = Circle((0, 0), radius=0, color='b', fill=False, linewidth=2)
ax.add_patch(circle)


def init():
    circle.set_radius(0)
    return circle,

def update(frame):
    current_t = frame * (T_MAX / NUM_FRAMES)
    
    new_radius = a * current_t
    
    circle.set_radius(new_radius)
   
    return circle,


ani = animation.FuncAnimation(
    fig, 
    update, 
    frames=NUM_FRAMES, 
    init_func=init, 
    interval=50, 
    blit=True 
)


plt.show() 


ani.save('expanding_circle.gif', writer='pillow', fps=30)

