# A numerical solution of 1D Gaussian advection equation by Upwind Scheme.

import matplotlib.pyplot as pl
import numpy as np
from matplotlib.animation import FuncAnimation

t0 = 0.0
dt = 0.1
t_final = 2
x0 = -2.0
dx = 0.1
x_max = 4.0
T = np.arange(t0, t_final+dt, dt)
X = np.arange(x0, x_max+dx, dx)
U = [0.0 for _ in X]
fig, ax = pl.subplots()
nframe = 0

for t in T:
    if t == t0:
        for i in range(len(X)):
            U[i] = np.exp(-X[i]**2)
    else:
        U_prime = [0.0 for _ in X]
        for i in range(len(X)):
            if i == 0:
                U_prime[i] = np.exp(-(x0-(1-np.cos(t)))**2)
            elif i == len(X)-1:
                U_prime[i] = np.exp(-(x_max-(1-np.cos(t)))**2)
            else:
                a = np.sin(t)
                if a > 0:
                    U_prime[i] = U[i] - a*dt/dx*(U[i] - U[i-1])
                else:
                    U_prime[i] = U[i] - a*dt/dx*(U[i+1] - U[i])
        U = U_prime
    ax.clear()
    line, = ax.plot(X, U, 'b-', linewidth=3)
    ax.set_xlabel('x')
    ax.set_ylabel('u')
    ax.set_xlim([x0, x_max])
    fig.savefig('upwind1d/frame_'+"%03d" % nframe+'.png')
    nframe += 1

# To generate GIF: convert frame_* GaussianUpwind1D.gif

    
