# A 3D Euler method based simulation of the Chua Attractor.
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pl
import numpy as np

t0 = 0.0
dt = 0.001
t_final = 100
T = np.arange(t0, t_final, dt)
alpha, beta, c, d = 15.6, 28.0, -0.714, -1.143
ax = pl.figure().add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

x, y, z = 0.7, 0, 0
for t in T:
    f = c*x + 0.5*(d-c)*(abs(x+1)-abs(x-1))
    new_x = x + alpha*(y-x-f) * dt
    new_y = y + (x - y + z) * dt
    new_z = z - beta * y * dt
    ax.plot([x, new_x], [y, new_y], [z, new_z], 'b-', linewidth=0.5)
    x, y, z = new_x, new_y, new_z

pl.show()
