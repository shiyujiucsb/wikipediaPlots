# A simulation of 1D Ito process with time step dt = .0001
# mu is zero. sigma is a Ricker wavelet.
import matplotlib.pyplot as pl
import numpy as np

t0 = 0.0
dt = 0.0001
t_final = 10.0
T = np.arange(t0, t_final, dt)
ax = pl.figure().add_subplot(111)
ax.set_xlabel('t')
ax.set_ylabel('X')

x = 0.0
mu = 0.0
# Ito Integral
np.random.seed(1)

def Ricker(t):
    return 2.0/(np.sqrt(3)*(np.pi**.25))*(1-t*t)*np.exp(-0.5*t*t)

for t in T:
    sigma = Ricker(t-t_final/2.0)
    new_x = x + mu*dt + sigma * np.random.normal(0, dt)
    ax.plot([t, t+dt], [x, new_x], 'b-', linewidth=0.5)
    x = new_x

pl.show()
