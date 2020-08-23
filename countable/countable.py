
import math
import time

def a(i,j):
    return i*j

# sets:
# A_1 = {1, 2, 3, 4, ...}
# A_2 = {2, 4, 6, 8, ...}
# A_3 = {3, 6, 9, 12, ...}

A_union = {}

diagonal = 0
while diagonal < math.inf: # i.e. for diagonal in {0,1,2,3,...}
    print(f"------- diagonal {diagonal} --------")
    for row in range(diagonal+1):
        col = diagonal - row
        print(f"A_{{{row},{col}}} = {a(row,col)}", end="\t\t")
        if A_union.get(a(row, col)):
            print("duplicate, not adding it to the set")
        else:
            print("new! adding it to the set")
            A_union[a(row, col)] = True
    diagonal += 1
    time.sleep(0.1)


