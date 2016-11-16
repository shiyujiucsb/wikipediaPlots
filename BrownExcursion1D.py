# A realization of 1D Brownian Excursion process time step dt = .0001

import matplotlib.pyplot as pl
import numpy as np

t0 = 0.0
dt = 0.0001
t_final = 1.0
T = np.arange(t0, t_final, dt)
ax = pl.figure().add_subplot(111)
ax.set_xlabel('t')
ax.set_ylabel('X')

np.random.seed(3)

while True:
    B = [0.0]
    for _ in range(len(T)):
        old_value = B[-1]
        new_value = old_value + np.random.normal(0, dt)
        B.append(new_value)

    W1 = B[-1]
    for i in range(len(B)):
        B[i] = B[i] - dt*i*W1
    if min(B) > -1e-14:
        break

for i in range(1,len(B)):
    ax.plot([dt*i, dt*(i-1)], [B[i], B[i-1]], 'b-', linewidth=0.5)

pl.show()
