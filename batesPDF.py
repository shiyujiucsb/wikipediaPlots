# PDF of Bates Distribution

import matplotlib.pyplot as pl
import numpy as np
import matplotlib.patches as mpatches

t0 = 0.0
dt = 0.001
t_final = 1.0
T = np.arange(t0, t_final, dt)
ax = pl.figure().add_subplot(111)

def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def comb(n, k):
    assert (n>=k)
    return factorial(n)/factorial(k)/factorial(n-k)

def f(x, n):
    sum = 0
    k = 0
    while k <= n*x:
        term = comb(n, k)*((n*x-k)**(n-1))
        if k%2==1:
            term = -term
        sum += term
        k += 1
    return sum*n/factorial(n-1)

def pdf(ax, n, color):
    for t in T:
        old_value = f(t, n)
        new_value = f(t+dt, n)
        ax.plot([t, t+dt], [old_value, new_value], color, linewidth=1.0)

ax.set_ylim([0, 7])
pdf(ax, 1, 'm-')
pdf(ax, 2, 'k-')
pdf(ax, 3, 'b-')
pdf(ax, 10, 'g-')
pdf(ax, 20, 'r-')

magentaPatch = mpatches.Patch(color='magenta', label='$n=1$')
blackPatch = mpatches.Patch(color='black', label='$n=2$')
bluePatch = mpatches.Patch(color='blue', label='$n=3$')
greenPatch = mpatches.Patch(color='green', label='$n=10$')
redPatch = mpatches.Patch(color='red', label='$n=20$')
pl.legend(handles = [magentaPatch, blackPatch, bluePatch, greenPatch, redPatch], loc=2)

pl.show()
