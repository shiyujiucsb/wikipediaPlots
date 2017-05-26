# CDF of Voigt Distribution

import matplotlib.pyplot as pl
import numpy as np
from scipy.special import wofz
import scipy.integrate as integral
import matplotlib.patches as mpatches
from math import pi

t0 = -10.0
dt = 0.01
t_final = 10.0
T = np.arange(t0, t_final, dt)
ax = pl.figure().add_subplot(111)

def V(sigma, gamma, x):
    z = (x + 1j * gamma) / (sigma * (2**0.5))
    return wofz(z).real / (sigma * (2*pi)**0.5)

def cdf(ax, sigma, gamma, color):
    for t in T:
        old_value = integral.quad(lambda x: V(sigma, gamma, x), -100, t)
        new_value = integral.quad(lambda x: V(sigma, gamma, x), -100, t+dt)
        ax.plot([t, t+dt], [old_value, new_value], color, linewidth=1.0)

cdf(ax, 1.53, 0.00, 'k-')
cdf(ax, 1.30, 0.50, 'b-')
cdf(ax, 1.00, 1.00, 'g-')
cdf(ax, 0.01, 1.80, 'r-')

blackPatch = mpatches.Patch(color='black', label='$\sigma=1.53, \gamma=0.00$')
bluePatch = mpatches.Patch(color='blue', label='$\sigma=1.30, \gamma=0.50$')
greenPatch = mpatches.Patch(color='green', label='$\sigma=1.00, \gamma=1.00$')
redPatch = mpatches.Patch(color='red', label='$\sigma=0.01, \gamma=1.80$')
pl.legend(handles = [blackPatch, bluePatch, redPatch, greenPatch], loc=2)

pl.show()