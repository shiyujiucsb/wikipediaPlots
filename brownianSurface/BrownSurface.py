# A realization of Brownian surface with step = 0.01
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pl
import numpy as np

x0, y0 = 0.0, 0.0
delta = 0.001
R = 2.0
x_final, y_final = R, R
X = np.arange(x0, x_final+delta, delta)
Y = np.arange(y0, y_final+delta, delta)
H = .8
fig = pl.figure()
ax = fig.add_subplot(111, projection='3d')

np.random.seed(0)

Gamma = [[0.0 for _ in Y] for _ in X]
for i in range(len(X)):
    for j in range(len(Y)):
        if 2*H <= 1.5:
            beta, c2, c0 = 0.0, H, 1-H
        else:
            beta = 2*H*(2-2*H)/(3*R*(R*R-1))
            c2 = (2*H-beta*(R-1)*(R-1)*(R+2))/2
            c0 = beta*(R-1)**3+1.0-c2
        r = (X[i]**2+Y[j]**2)**0.5
        if r<=1:
            Gamma[i][j] = c0-r**(2*H)+c2*r*r
        elif r<=R:
            Gamma[i][j] = beta*(R-r)**3/r
        else:
            Gamma[i][j] = 0

eigens, P = np.linalg.eig(Gamma)

Lambda = [[0.0 for _ in Y] for _ in X]
for i in range(len(Lambda)):
    Lambda[i][i] = eigens[i]**0.25

Sigma = np.matmul(np.matmul(P, Lambda), np.matrix.transpose(P))

surface = [[np.random.normal(0, 1) for _ in Y] for _ in X]

surface = np.matmul(Sigma, surface)

x_final, y_final = R/2, R/2
X = np.arange(x0, x_final+delta, delta)
Y = np.arange(y0, y_final+delta, delta)
Results = [[0.0 for _ in Y] for _ in X]
for i in range(len(X)):
    for j in range(len(Y)):
        Results[i][j] = surface[i][j]
X, Y = np.meshgrid(X, Y)
ax.plot_surface(X, Y, Results, cmap="summer", lw=0.0)

pl.show()
