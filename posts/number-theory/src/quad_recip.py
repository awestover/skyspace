import matplotlib.pyplot  as plt

p = 101
q = 223

def typeRed(x,y):
    return q*y-p*x >= q/2
def typeBlue(x,y):
    return q*y-p*x <= -p/2
def typeBlack(x,y):
    return not typeRed(x,y) and not typeBlue(x,y)

def unpack(array):
    flat = []
    for L in array:
        flat += L
    xs = [pair[0] for pair in flat]
    ys = [pair[1] for pair in flat]
    return xs, ys

def typeXs(typeFn):
    type_matrix = [[(x,y) for x in range(q//2) if typeFn(x,y)] for y in range(p//2)]
    return unpack(type_matrix)

plt.scatter(*typeXs(typeRed), c='r', alpha=.5)
plt.scatter(*typeXs(typeBlue), c='b', alpha=.5)
plt.scatter(*typeXs(typeBlack), c='k')
plt.show()

