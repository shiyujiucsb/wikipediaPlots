# A simulation of 2D Drifted Wiener process with time step dt = .0001
import matplotlib.pyplot as pl
import numpy as np

t0 = 0.0
dt = 0.0001
t_final = 3.9
T = np.arange(t0, t_final, dt)
ax = pl.figure().add_subplot(111)
ax.set_xlabel('X')
ax.set_ylabel('Y')

x = 0.0
sigma = 100.0
# Ito Integral
np.random.seed(2)
for t in T:
    new_x = x + sigma * np.random.normal(0, dt)
    ax.plot([t, t+dt], [(x*x-t)/2, (new_x*new_x-t-dt)/2], 'b-', linewidth=0.5)
    x = new_x

# sigma * dW process
x = 0.0
np.random.seed(2)
for t in T:
    new_x = x + sigma * np.random.normal(0, dt)
    ax.plot([t, t+dt], [x, new_x], 'r-', linewidth=0.5)
    x = new_x

pl.show()
