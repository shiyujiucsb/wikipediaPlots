# A 3D Euler method based simulation of the Modified Chua Attractor.
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pl
import numpy as np

t0 = 0.0
dt = 0.01
t_final = 1000
T = np.arange(t0, t_final, dt)
alpha, beta = 10.82, 14.286
a, b, c, d = 1.3, .11, 7, 0
ax = pl.figure().add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

x, y, z = 1, 1, 0
for t in T:
    h = -b*np.sin(np.pi*x/(2*a)+d)
    new_x = x + alpha*(y-h) * dt
    new_y = y + (x - y + z) * dt
    new_z = z - beta * y * dt
    ax.plot([x, new_x], [y, new_y], [z, new_z], 'b-', linewidth=0.5)
    x, y, z = new_x, new_y, new_z

pl.show()
