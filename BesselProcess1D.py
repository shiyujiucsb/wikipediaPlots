# A realization of 1D Bessel process with n = 3, 10, 20 and time step dt = .0001

import matplotlib.pyplot as pl
import numpy as np
import matplotlib.patches as mpatches

t0 = 0.0
dt = 0.0001
t_final = 2.0
T = np.arange(t0, t_final, dt)
ax = pl.figure().add_subplot(111)
ax.set_xlabel('t')
ax.set_ylabel('X')

def realize(ax, n, color):
    B = [0.0 for _ in range(n)]
    np.random.seed(1)

    for t in T:
        old_value = np.sqrt(sum([x*x for x in B]))
        for i in range(len(B)):
            B[i] += np.random.normal(0, dt)
        new_value = np.sqrt(sum([x*x for x in B]))
        ax.plot([t, t+dt], [old_value, new_value], color, linewidth=0.5)

realize(ax, 3, 'b-')
realize(ax, 10, 'r-')
realize(ax, 20, 'g-')

bluePatch = mpatches.Patch(color='blue', label='$n = 3$')
redPatch = mpatches.Patch(color='red', label='$n = 10$')
greenPatch = mpatches.Patch(color='green', label='$n = 20$')
pl.legend(handles = [bluePatch, redPatch, greenPatch], loc=2)

pl.show()
