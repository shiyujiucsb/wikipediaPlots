# Beta distribution mode when alpha, beta in [1, 5].
# Idea from Dr. J. Rodal
# Use Inkscape to enlarge and adjust the figure position 
# (degroup, enlarge and regroup the SVG elements etc.).

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pl
from matplotlib import cm
import numpy as np
from scipy.special import betainc
import scipy.integrate as integral

# Prepare the data by the mode
A = np.arange(1.01, 5.0, .01)
B = np.arange(1.01, 5.0, .01)
gridA, gridB = np.meshgrid(A, B)
Z = np.ndarray(shape=gridA.shape, dtype = float)
for i in range(len(A)):
  for j in range(len(B)):
    Z[j][i] = (A[i] - 1) / (A[i] + B[j] - 2)
# Draw the data
fig = pl.figure()
ax = fig.add_subplot(111, projection = '3d')
pl.xticks([1.0, 2.0, 3.0, 4.0, 5.0])
pl.yticks([1.0, 2.0, 3.0, 4.0, 5.0])
ax.contour(gridA, gridB, Z, zdir='z', offset=0)
ax.plot_surface(gridA, gridB, Z, lw = 0.0)
ax.plot_wireframe(gridA, gridB, Z, lw = 1.0, color = 'black', \
   rstride=20, cstride=20)
ax.set_xlim([1.0, 5.0])
ax.set_ylim([1.0, 5.0])
ax.set_zlim([0, 1.0])
ax.set_xlabel('alpha')
ax.set_ylabel('beta')
ax.set_zlabel('Mode')
ax.view_init(30,120)
fig.savefig('betaDistrMode.svg')

