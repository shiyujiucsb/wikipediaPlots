# An Euler method based simulation of the PWL Duffing chaotic Attractor with i=-15.
import matplotlib.pyplot as pl
import numpy as np

t0 = 0.0
dt = 0.01
t_final = 1000
T = np.arange(t0, t_final, dt)
i,e = -14.0, .25
gamma, m0, m1, omega, c = .14+i/20, -.0845, .66, 1.0, .14+i/20
ax = pl.figure().add_subplot(111)
ax.set_xlabel('X')
ax.set_ylabel('Y')

x, y = 0.0, 0.0
for t in T:
    new_x = x + y * dt
    new_y = y + (-m1*x - (m0-m1)/2*(abs(x+1)-abs(x-1)) - e*y + gamma*np.cos(omega*t)) * dt
    ax.plot([x, new_x], [y, new_y], 'b-', linewidth=0.5)
    x, y = new_x, new_y
pl.axis('off')
pl.show()
