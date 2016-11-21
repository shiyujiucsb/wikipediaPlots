# A realization of Brownian surface with step = 0.01
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pl
import numpy as np

x0, y0 = 0.0, 0.0
delta = 0.005
x_final, y_final = 1.0, 1.0
X = np.arange(x0, x_final+delta, delta)
Y = np.arange(y0, y_final+delta, delta)
H = .5
ax = pl.figure().add_subplot(111, projection='3d')

np.random.seed(0)

Gamma = [[0.0 for _ in Y] for _ in X]
for i in range(len(X)):
    for j in range(len(Y)):
        Gamma[i][j] = 0.5*(X[i]**(2*H) + Y[j]**(2*H) - abs(X[j]-Y[i])**(2*H))

eigens, P = np.linalg.eig(Gamma)

Lambda = [[0.0 for _ in Y] for _ in X]
for i in range(len(Lambda)):
    Lambda[i][i] = eigens[i]**0.5

Sigma = np.matmul(np.matmul(P, Lambda), np.matrix.transpose(P))

surface = [[np.random.normal(0, 1) for _ in Y] for _ in X]

surface = np.matmul(Sigma, surface)

X, Y = np.meshgrid(X, Y)
ax.plot_surface(X, Y, surface, cmap="summer", lw=0.1)

pl.show()
