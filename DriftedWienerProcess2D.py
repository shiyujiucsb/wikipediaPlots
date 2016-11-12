# A simulation of 2D Ito process with time step dt = .0001
import matplotlib.pyplot as pl
import numpy as np

t0 = 0.0
dt = 0.0001
t_final = 2
T = np.arange(t0, t_final, dt)
ax = pl.figure().add_subplot(111)
ax.set_xlabel('X')
ax.set_ylabel('Y')

x, y = 0.0, 0.0
mu = .02
sigma = 1.0
# Drifted
np.random.seed(1)
for t in T:
    new_x = x + mu*dt + sigma * np.random.normal(0, dt)
    new_y = y + mu*dt + sigma * np.random.normal(0, dt)
    ax.plot([x, new_x], [y, new_y], 'b-', linewidth=0.5)
    x, y = new_x, new_y

# Wiener's
x, y = 0.0, 0.0
np.random.seed(1)
for t in T:
    new_x = x + sigma * np.random.normal(0, dt)
    new_y = y + sigma * np.random.normal(0, dt)
    ax.plot([x, new_x], [y, new_y], 'r-', linewidth=0.5)
    x, y = new_x, new_y

pl.show()
