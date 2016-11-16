# Two realizations of Geometric Brownian process with time step dt = .0001

import matplotlib.pyplot as pl
import numpy as np
import matplotlib.patches as mpatches

t0 = 0.0
dt = 0.0001
t_final = 1.0
T = np.arange(t0, t_final, dt)
ax = pl.figure().add_subplot(111)
ax.set_xlabel('t')
ax.set_ylabel('X')

np.random.seed(1)

def drawMotion(mu, sigma, color):
    x = 1.0
    for t in T:
        new_x = x + mu*x*dt + sigma*x*np.random.normal(0, dt)
        ax.plot([t, t+dt], [x, new_x], color, linewidth=0.5)
        x = new_x

drawMotion(1, 20, 'b-')
drawMotion(0.5, 50, 'g-')

bluePatch = mpatches.Patch(color='blue', label='$\mu = 1$, $\sigma = 20$')
greenPatch = mpatches.Patch(color='green', label='$\mu = 0.5$, $\sigma = 50$')
pl.legend(handles = [bluePatch, greenPatch], loc=2)

pl.show()
