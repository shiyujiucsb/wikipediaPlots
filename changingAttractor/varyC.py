# An Euler method based simulation to compute the bifurcation of the Rossler system.
import matplotlib.pyplot as pl
from matplotlib.lines import Line2D
import numpy as np

t0 = 0.0
dt = 0.001
t_final = 1500
T = np.arange(t0, t_final, dt)
a, b = 0.1, 0.1
ax = pl.figure().add_subplot(111)
pl.xlim([0, 45])
pl.ylim([0, 70])
pl.xlabel('c')
pl.ylabel('X')

C = []
X = []
e = 1e-2
c = 0.0
while c < 45.0:
    x, y, z = 5.8, 1.0, 0.0
    counter = 10
    # the first 10 points may contain outliers
    for t in T:
        new_x = x + (-y - z) * dt
        new_y = y + (x + a*y) * dt
        new_z = z + (b + z*(x-c)) * dt
        if 0<new_x<70 and abs(new_y)<e:
            if counter==0:
                C.append(c)
                X.append(new_x)
            else:
                counter-=1
        x, y, z = new_x, new_y, new_z
    c += 0.1

pl.scatter(C, X, .1, color='red')
pl.show()
#pl.savefig('./varyC.svg')
