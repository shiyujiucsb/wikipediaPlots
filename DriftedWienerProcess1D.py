# A simulation of 1D Wiener process with/without drift with time step dt = .0001
import matplotlib.pyplot as pl
import numpy as np

t0 = 0.0
dt = 0.0001
t_final = 2
T = np.arange(t0, t_final, dt)
ax = pl.figure().add_subplot(111)
ax.set_xlabel('t')
ax.set_ylabel('X')

x = 0.0
mu = 1
sigma = 100.0
# Drifted
np.random.seed(2)
for t in T:
    new_x = x + mu*dt + sigma * np.random.normal(0, dt)
    ax.plot([t, t+dt], [x, new_x], 'b-', linewidth=0.5)
    x = new_x

# sigma * dW process
x = 0.0
np.random.seed(2)
for t in T:
    new_x = x + sigma * np.random.normal(0, dt)
    ax.plot([t, t+dt], [x, new_x], 'r-', linewidth=0.5)
    x = new_x

pl.show()
