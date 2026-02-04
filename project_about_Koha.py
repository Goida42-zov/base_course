import numpy as np
import matplotlib.pyplot as plt

def koch_step(segment):
    start, end = segment
    one_third = (end - start) / 3
    point1 = start + one_third
    point2 = start + 2 * one_third


    angle = np.pi / 3
    rotation = np.array([[np.cos(angle), -np.sin(angle)],
                         [np.sin(angle),  np.cos(angle)]])
    peak = point1 + rotation @ one_third

    return [[start, point1], [point1, peak], [peak, point2], [point2, end]]


p_start = np.array([0.0, 0.0])
p_end   = np.array([1.0, 0.0])
segments = [[p_start, p_end]]


depth = 4
for _ in range(depth):
    new_segments = []
    for seg in segments:
        new_segments.extend(koch_step(seg))
    segments = new_segments


plt.figure(figsize=(10,4))
for seg in segments:
    x = [seg[0][0], seg[1][0]]
    y = [seg[0][1], seg[1][1]]
    plt.plot(x, y, color='blue', lw=2)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Криявя Коха')
plt.axis('equal')
plt.savefig('koch_curve.png')
plt.show()
