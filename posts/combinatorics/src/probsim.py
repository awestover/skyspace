import matplotlib.pyplot as plt
import numpy as np

p = 0.45
def val(n):
    A = np.array([[0.0 for i in range(n+1)] for j in range(n+1)])
    b = np.array([1.0 for i in range(n+1)])
    b[n] = 0

    A[0][0] = 1
    A[0][1] = -1

    for i in range(1,n):
        A[i][i] = 1
        A[i][i-1] = -(1-p)
        A[i][i+1] = -p

    A[n][n] = 1

    F = np.linalg.solve(A,b)

    return F[0]

NS = range(2,100)
vals = [val(n) for n in NS]
eps = 1/2 -p
bob = (1+2*eps)/(1-2*eps)
points = [bob**(1.1*n) for n in NS]
plt.plot(vals)
plt.plot(points)
plt.show()

