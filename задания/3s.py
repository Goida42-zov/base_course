import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_5_point_star_points(center_x, center_y, outer_radius, inner_radius):
    points = []
    for i in range(10):
        radius = outer_radius if i % 2 == 0 else inner_radius
        angle = np.deg2rad(i * 36 + 90)
        x = center_x + radius * np.cos(angle)
        y = center_y + radius * np.sin(angle)
        points.append((x, y))
    return np.array(points)

center_x, center_y = 20, 40
outer_radius = 20
inner_radius = 8
xlim_min, xlim_max = -25, 25 
ylim_min, ylim_max = -25, 25 

star_points_static = generate_5_point_star_points(0, 0, outer_radius, inner_radius)

fig, ax = plt.subplots(figsize=(8, 8))

ax.set_xlim(xlim_min + center_x - 5, xlim_max + center_x + 5) 
ax.set_ylim(ylim_min + center_y - 5, ylim_max + center_y + 5)

ax.set_aspect('equal', adjustable='box')
ax.set_title('Вращающаяся Пятиконечная Звезда')
ax.grid(True)

line, = ax.plot(np.append(star_points_static[:, 0], star_points_static), 
                np.append(star_points_static[:, 1], star_points_static), 
                lw=5, color='blue')

def init():
    line.set_data([], [])
    return line,

def update(frame):
    alpha = 2 * np.pi * frame / 100 
    
    rotated_x = star_points_static[:, 0] * np.cos(alpha) - star_points_static[:, 1] * np.sin(alpha)
    rotated_y = star_points_static[:, 0] * np.sin(alpha) + star_points_static[:, 1] * np.cos(alpha)
    
    final_x = rotated_x + center_x
    final_y = rotated_y + center_y
    
    line.set_data(np.append(final_x, final_x), np.append(final_y, final_y))
    return line,

ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)

plt.show()
ani.save('rotating_star.gif', writer='pillow', fps=30)