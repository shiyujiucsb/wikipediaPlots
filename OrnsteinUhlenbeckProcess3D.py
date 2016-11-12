# A simulation of 3D Ornstein-Uhlenbeck process with time step dt = .0001
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pl
import numpy as np

t0 = 0.0
dt = 0.0001
t_final = 2
T = np.arange(t0, t_final, dt)
ax = pl.figure().add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

x, y, z = 10.0, 10.0, 10.0
ux, uy, uz = 0.0, 0.0, 0.0
theta = 1.0
sigma = 300.0
np.random.seed(1)
for t in T:
    new_x = x + theta*(ux-x)*dt + sigma * np.random.normal(0, dt)
    new_y = y + theta*(uy-y)*dt + sigma * np.random.normal(0, dt)
    new_z = z + theta*(uz-z)*dt + sigma * np.random.normal(0, dt)
    ax.plot([x, new_x], [y, new_y], [z, new_z], 'b-', linewidth=0.5)
    x, y, z = new_x, new_y, new_z

pl.show()
