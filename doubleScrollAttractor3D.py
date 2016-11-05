# A 3D Euler method based simulation of the Double Scroll system.
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pl
import numpy as np

t0 = 0.0
dt = 0.001
t_final = 100
T = np.arange(t0, t_final, dt)
a, b, c = 40, 3, 28
ax = pl.figure().add_subplot(111, projection='3d')
ax.set_xlim([-40, 40])
ax.set_ylim([-30, 30])
ax.set_zlim([0, 40])
ax.set_xticks(np.arange(-40,40,10))
ax.set_yticks(np.arange(-30,30,10))
ax.set_zticks(np.arange(0,50,10))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

x, y, z = -0.1, 0.5, -0.6
for t in T:
    new_x = x + a*(y-x) * dt
    new_y = y + ((c-a)*x - x*z + c*y) * dt
    new_z = z + (x*y - b*z) * dt
    ax.plot([x, new_x], [y, new_y], [z, new_z], 'b-', linewidth=0.5)
    x, y, z = new_x, new_y, new_z

pl.show()
