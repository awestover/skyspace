import matplotlib.pyplot as plt
from math import comb, sqrt, log2, e

n = 100
idxs = list(range(n//10,n//2))
actual = [1 for k in range(n)]
log_estimate = []
for k in range(1,n):
  actual[k] = actual[k-1] + comb(n, k)

  eps = k/n
  log_estimate.append( log2(2/sqrt(e)) + eps*log2(e/(2*eps)) ) 

log_actual = [log2(a)/n for a in actual]
ratio = [log_estimate[i]/log_actual[i] for i in idxs]

plt.plot(idxs, ratio)
plt.show()

