# An Euler method based simulation of the Henon Map.
import matplotlib.pyplot as pl
import numpy as np

t_final = 50000
a, b, = 1.4, 0.3
ax = pl.figure().add_subplot(111)

x, y = 0.0, 0.0
for t in range(t_final):
    ax.scatter(x, y, .1, color='black')
    new_x = 1 - a*x*x + y
    new_y = b*x
    x, y = new_x, new_y

pl.axis('off')
pl.show()
