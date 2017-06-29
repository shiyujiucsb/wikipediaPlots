# PDF of ARGUS Distribution

import matplotlib.pyplot as pl
import numpy as np
from scipy.special import wofz
import matplotlib.patches as mpatches
import scipy.integrate as integral
from math import pi
from math import exp

t0 = 0.0
dt = 0.001
t_final = 1.0 # also c
c = t_final
T = np.arange(t0, t_final, dt)
ax = pl.figure().add_subplot(111)

# standard normal distribution pdf
def phi(x):
    return exp(-0.5*x*x)/((2*pi)**0.5)

# standard normal distribution cdf
def Phi(x):
    return integral.quad(lambda t: phi(t), -100, x)[0]

def f(x, chi, c):
    return (chi**3)/((Phi(chi)-chi*phi(chi)-0.5) \
            *(2*pi)**0.5)*x/c/c*((1.0-x*x/c/c)**0.5) \
            *exp(-chi*chi*(1.0-x*x/c/c)/2.0)

def pdf(ax, chi, c, color):
    for t in T:
        old_value = f(t, chi, c)
        new_value = f(t+dt, chi, c)
        ax.plot([t, t+dt], [old_value, new_value], color, linewidth=1.0)

pdf(ax, 0.1, c, 'm-')
pdf(ax, 0.5, c, 'k-')
pdf(ax, 1.0, c, 'b-')
pdf(ax, 2.0, c, 'g-')
pdf(ax, 3.0, c, 'r-')

magentaPatch = mpatches.Patch(color='magenta', label='$\chi=0.1$')
blackPatch = mpatches.Patch(color='black', label='$\chi=0.5$')
bluePatch = mpatches.Patch(color='blue', label='$\chi=1.0$')
greenPatch = mpatches.Patch(color='green', label='$\chi=2.0$')
redPatch = mpatches.Patch(color='red', label='$\chi=3.0$')
pl.legend(handles = [magentaPatch, blackPatch, bluePatch, greenPatch, redPatch], loc=2)

pl.show()
