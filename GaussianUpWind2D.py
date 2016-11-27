# A numerical solution of 2D Gaussian advection equation by Upwind Scheme.
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pl
import numpy as np

t0 = 0.0
dt = 0.045
t_final = 1
x0 = -2.0
dx = 0.04
x_max = 4.0
y0 = -2.0
dy = 0.04
y_max = 4.0
T = np.arange(t0, t_final+dt, dt)
X = np.arange(x0, x_max+dx, dx)
Y = np.arange(y0, y_max+dy, dy)
U = [[0.0 for _ in Y] for _ in X]
fig = pl.figure()
ax = fig.add_subplot(111, projection='3d')
nframe = 0

for t in T:
    if t == t0:
        for i in range(len(X)):
            for j in range(len(Y)):
                U[i][j] = np.exp(-X[i]**2-Y[j]**2)
    else:
        U_prime = [[0.0 for _ in Y] for _ in X]
        for i in range(len(X)):
            for j in range(len(Y)):
                if i == 0 or j == 0 or i == len(X)-1 or j == len(Y)-1:
                    U_prime[i][j] = np.exp(-(X[i]-(1-np.cos(t)))**2-(Y[j]-np.sin(t))**2)
                else:
                    ux = np.sin(t)
                    uy = np.cos(t)
                    if ux > 0 and uy > 0:
                        U_prime[i][j] = U[i][j] - ux*dt/dx*(U[i][j] - U[i-1][j]) - uy*dt/dy*(U[i][j] - U[i][j-1])
                    elif ux > 0 and uy <= 0:
                        U_prime[i][j] = U[i][j] - ux*dt/dx*(U[i][j] - U[i-1][j]) - uy*dt/dy*(U[i][j+1] - U[i][j])
                    elif ux <= 0 and uy > 0:
                        U_prime[i][j] = U[i][j] - ux*dt/dx*(U[i+1][j] - U[i][j]) - uy*dt/dy*(U[i][j] - U[i][j-1])
                    else:
                        U_prime[i][j] = U[i][j] - ux*dt/dx*(U[i+1][j] - U[i][j]) - uy*dt/dy*(U[i][j+1] - U[i][j])
        U = U_prime
        
    ax.clear()
    gridX, gridY = np.meshgrid(X, Y)
    ax.plot_surface(gridX, gridY, U, cmap = 'summer', lw = 0.0)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('phi')
    ax.set_xlim([x0, x_max])
    ax.set_ylim([y0, y_max])
    ax.set_zlim([0, 1])
    fig.savefig('upwind2d/frame_'+"%03d" % nframe+'.png')
    nframe += 1

# To generate GIF: convert frame_* GaussianUpwind2D.gif

    
