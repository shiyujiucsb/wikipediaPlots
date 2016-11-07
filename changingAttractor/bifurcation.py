# An Euler method based simulation to compute the bifurcation of the Rossler system.
import matplotlib.pyplot as pl
from matplotlib.lines import Line2D
import numpy as np

t0 = 0.0
dt = 0.001
t_final = 300
T = np.arange(t0, t_final, dt)
a, c = 0.2, 5.7
ax = pl.figure().add_subplot(111)
pl.xlim([0, 2])
pl.ylim([2, 15])
pl.xlabel('b')
pl.ylabel('X')

B = []
X = []
e = 1e-2
b = 0.0
while b < 2.0:
    x, y, z = 5.8, 1.0, 0.0
    counter = 100
    # the first 100 points may contain outliers
    for t in T:
        new_x = x + (-y - z) * dt
        new_y = y + (x + a*y) * dt
        new_z = z + (b + z*(x-c)) * dt
        if 2<new_x<15 and abs(new_y)<e:
            if counter==0:
                B.append(b)
                X.append(new_x)
            else:
                counter-=1
        x, y, z = new_x, new_y, new_z
    b += 0.001

pl.scatter(B, X, .01, color='red')
pl.show()
#pl.savefig('./rosslerBifurcation.svg')
