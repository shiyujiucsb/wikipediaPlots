# A 3D Euler method based simulation of the Modified Lorenz System.
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pl
import numpy as np

t0 = 0.0
dt = 0.001
t_final = 100
T = np.arange(t0, t_final, dt)
a, b, c = 10.0, 8.0/3, 137.0/5
ax = pl.figure().add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

x, y, z = -8.0, 4.0, 10.0
for t in T:
    f = 1.0/3/np.sqrt(x*x+y*y)
    dx = 1.0/3*(-(a+1)*x+a-c+z*y) + ((1-a)*(x*x-y*y) + (2*(a+c-z))*x*y)*f
    dy = 1.0/3*((c-a-z)*x-(a+1)*y) + (2*(a-1)*x*y + (a+c-z)*(x*x-y*y))*f
    dz = 0.5*(3*x*x*y - y*y*y) - b*z
    new_x = x + dx * dt
    new_y = y + dy * dt
    new_z = z + dz * dt
    ax.plot([x, new_x], [y, new_y], [z, new_z], 'b-', linewidth=0.5)
    x, y, z = new_x, new_y, new_z

pl.show()
