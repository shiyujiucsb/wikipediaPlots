# Beta distribution median given alpha and beta.
# Idea from Dr. J. Rodal
# Use Inkscape to enlarge and adjust the figure position 
# (degroup, enlarge and regroup the SVG elements etc.).

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pl
from matplotlib import cm
import numpy as np
from scipy.special import betainc
import scipy.integrate as integral

# binary search the root I_x(alpha, beta) = 0.5
def binary_search(a, b, result, err):
  low, high = 0.0, 1.0
  while low + err < high:
    mid = (low + high)/2.0
    if abs(betainc(a, b, mid) - result) < err:
      return mid
    elif betainc(a, b, mid) < result:
      low = mid
    else: high = mid
  return low

# Prepare the data by Ix(a, a)^[-1]
A = np.arange(0.01, 5.0, .01)
B = np.arange(0.01, 5.0, .01)
gridA, gridB = np.meshgrid(A, B)
Z = np.ndarray(shape=gridA.shape, dtype = float)
for i in range(len(A)):
  for j in range(len(B)):
    Z[j][i] = binary_search(A[i], B[j], 0.5, err = .001)
# Draw the data
fig = pl.figure()
ax = fig.add_subplot(111, projection = '3d')
pl.xticks([0.0, 2.0, 4.0])
pl.yticks([0.0, 2.0, 4.0])
ax.contour(gridA, gridB, Z, zdir='z', offset=0)
ax.plot_surface(gridA, gridB, Z, lw = 0.0)
ax.plot_wireframe(gridA, gridB, Z, lw = 1.0, color = 'black', \
   rstride=10, cstride=10)
ax.set_xlim([0.0, 5.0])
ax.set_ylim([0.0, 5.0])
ax.set_zlim([0, 1.0])
ax.set_xlabel('alpha')
ax.set_ylabel('beta')
ax.set_zlabel('Median')
ax.view_init(30,120)
fig.savefig('betaDistrMedian.svg')

