# A realization of 1D Fractional Brownian motion with time step dt = .5

import matplotlib.pyplot as pl
import numpy as np

t0 = 0.0
dt = 0.5
t_final = 1000.0
T = np.arange(t0, t_final+dt, dt)
H = .15
ax = pl.figure().add_subplot(111)
ax.set_xlabel('t')
ax.set_ylabel('X')

np.random.seed(0)

Gamma = [[0.0 for _ in T] for _ in T]
for i in range(len(T)):
    for j in range(len(T)):
        Gamma[i][j] = 0.5*(T[i]**(2*H) + T[j]**(2*H) - abs(T[j]-T[i])**(2*H))

eigens, P = np.linalg.eig(Gamma)

Lambda = [[0.0 for _ in T] for _ in T]
for i in range(len(Lambda)):
    Lambda[i][i] = eigens[i]**0.5

Sigma = np.matmul(np.matmul(P, Lambda), np.matrix.transpose(P))

path = [np.random.normal(0, 1) for _ in T]

path = np.matmul(Sigma, path)

for i in range(1, len(T)):
    ax.plot([T[i-1], T[i]], [path[i-1], path[i]], 'k-', linewidth=0.5)

pl.show()
