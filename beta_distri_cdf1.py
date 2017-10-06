# Beta distribution CDF when alpha = beta.
# Idea from Dr. J. Rodal
# Use Inkscape to enlarge and adjust the figure position 
# (degroup, enlarge and regroup the SVG elements etc.).

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pl
from matplotlib import cm
import numpy as np
from scipy.special import beta, betainc
import scipy.integrate as integral
# Prepare the data by Ix(a, a)
X = np.arange(0.0,  1.0, .02)
A = np.arange(0.0, 20.0, .002)
gridX, gridA = np.meshgrid(X, A)
Z = np.ndarray(shape=gridX.shape, dtype = float)
for i in range(len(X)):
  for j in range(len(A)):
    if A[j] < 0.001: Z[j][i] = 0.5
    else:  Z[j][i] = betainc(A[j], A[j], X[i])
# Draw the data
fig = pl.figure()
ax = fig.add_subplot(111, projection = '3d')
pl.xticks([0.0, 0.5, 1.0])
pl.yticks([0.0, 5.0, 10.0, 15.0, 20.0])
ax.contour(gridX, gridA, Z, zdir='z', offset=0)
ax.plot_surface(gridX, gridA, Z, lw = 0.0)
ax.plot_wireframe(gridX, gridA, Z, lw = 1.0, color = 'black', \
   rstride=1000, cstride=10)
ax.set_xlim([0.0,  1.0])
ax.set_ylim([0.0, 20.0])
ax.set_zlim([0, 1.0])
ax.set_xlabel('x')
ax.set_ylabel('alpha')
ax.set_zlabel('CDF')
ax.view_init(30,250)
fig.savefig('betaDistrCDF1.svg')

