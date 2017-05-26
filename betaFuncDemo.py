# Beta function over [0.03, 4]^2.
# Use Inkscape to enlarge and adjust the figure position 
# (degroup, enlarge and regroup the SVG elements etc.).

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pl
import numpy as np
from scipy.special import beta

# Prepare the data by Beta(x, y)
X = np.arange(0.03, 4.0, .01)
Y = np.arange(0.03, 4.0, .01)
Z = np.ndarray(shape=(len(X), len(Y)), dtype = float)
for i in range(len(X)):
        for j in range(len(Y)):
                Z[i][j] = beta(X[i], Y[j])
# Draw the data
fig = pl.figure()
ax = fig.add_subplot(111, projection = '3d')
gridX, gridY = np.meshgrid(X, Y)
ax.plot_surface(gridX, gridY, Z, lw = 0.0)
pl.xticks([0, 1, 2, 3, 4])
pl.yticks([0, 1, 2, 3, 4])
ax.contour(X, Y, Z, zdir='z', offset=0)
ax.set_xlim([4.0, 0.0])
ax.set_ylim([4.0, 0.0])
ax.set_zlim([0, 50])
fig.savefig('betaFuncDemo.svg')
