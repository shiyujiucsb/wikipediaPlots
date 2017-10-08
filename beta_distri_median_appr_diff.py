# Beta distribution median-appr rel diff.
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

# Prepare the data.
A = np.arange(1.01, 5.0, .01)
B = np.arange(1.01, 5.0, .01)
gridA, gridB = np.meshgrid(A, B)
Z = np.ndarray(shape=gridA.shape, dtype = float)
for i in range(len(A)):
  for j in range(len(B)):
    median = binary_search(A[i], B[j], 0.5, err = 1e-7)
    appr   = (A[i] - 1/3.0) / (A[i] + B[j] - 2/3.0)
    Z[j][i] = abs(median - appr) / median
# Draw the data
fig = pl.figure()
ax = fig.add_subplot(111, projection = '3d')
pl.xticks([1, 2, 3, 4, 5])
pl.yticks([1, 2, 3, 4, 5])
ax.contour(gridA, gridB, Z, zdir='z', offset=-.45)
ax.plot_surface(gridA, gridB, Z, lw = 0.0)
ax.plot_wireframe(gridA, gridB, Z, lw = 1.0, color = 'black', \
   rstride=20, cstride=20)
ax.set_xlim([1.0, 5.0])
ax.set_ylim([1.0, 5.0])
ax.set_xlabel('alpha')
ax.set_ylabel('beta')
ax.set_zlabel('Rel. Error')
ax.view_init(20,30)
fig.savefig('betaDistrMedianApprDiff.svg')

