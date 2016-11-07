# An Euler method based simulation of the Rossler system (c=8.5, period 4).
import matplotlib.pyplot as pl
from matplotlib.lines import Line2D
import numpy as np

t0 = 0.0
dt = 0.008
t_final = 60
T = np.arange(t0, t_final, dt)
a, b, c = 0.1, 0.1, 8.5
ax = pl.figure().add_subplot(111)
pl.xlim([-15, 15])
pl.ylim([-15, 15])
pl.xlabel('X')
pl.ylabel('Y')

x, y, z = -8.65, 0.0, 0.0
for t in T:
    new_x = x + (-y - z) * dt
    new_y = y + (x + a*y) * dt
    new_z = z + (b + z*(x-c)) * dt
    line = Line2D([x, new_x], [y, new_y], color='blue', lw=0.5)
    ax.add_line(line)
    x, y, z = new_x, new_y, new_z

pl.show()
