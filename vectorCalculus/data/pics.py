import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(-10,10,10)
ys = np.linspace(-10,10,10)
Xs, Ys = np.meshgrid(xs, ys)
U = -Ys
V = Xs

plt.quiver(xs, ys, U, V, np.hypot(U, V))
plt.show() 

