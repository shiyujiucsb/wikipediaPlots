# A 3D Euler method based simulation of the Rossler system.
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pl
import numpy as np

t0 = 0.0
dt = 0.02
t_final = 60
T = np.arange(t0, t_final, dt)
a, b, c = 0.2, 0.2, 5.7
ax = pl.figure().add_subplot(111, projection='3d')
ax.set_xlim([-10, 15])
ax.set_ylim([-30, 10])
ax.set_zlim([0, 30])
ax.set_yticks(np.arange(-30, 10, 10))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# We consider many initial conditions.
for y in np.arange(-8,-3,1.0):
    x, z = 0.0, 0.0
    for t in T:
        new_x = x + (-y - z) * dt
        new_y = y + (x + a*y) * dt
        new_z = z + (b + z*(x-c)) * dt
        ax.plot([x, new_x], [y, new_y], [z, new_z], 'b-', linewidth=0.5)
        x, y, z = new_x, new_y, new_z
ax.scatter(0,0,0,color='red')

pl.show()
