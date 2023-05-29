# https://atcoder.jp/contests/abc298/tasks/abc298_b

import numpy as np
def hantei(a,n):
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and B[i][j] != 1:
                return 0
    return 1
 
n = int(input())
ch = 0
A = np.array([list(map(int, input().split())) for i in range(n)])
B = np.array([list(map(int, input().split())) for i in range(n)])
Arot1 = np.rot90(A)
Arot2 = np.rot90(Arot1)
Arot3 = np.rot90(Arot2)
if hantei(A,n) + hantei(Arot1,n) + hantei(Arot2,n) + hantei(Arot3,n) >= 1:
    print('Yes')
else:
    print('No')
