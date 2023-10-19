# https://atcoder.jp/contests/abc309/tasks/abc309_b

import numpy as np

n = int(input())
A = np.array([list(map(int,input().split())) for i in range(n)])

ue = A[0,:]
hi = A[:,0]
mi = A[:,n-1]
si = A[n-1,:]

print(hi)

ue_t = hi[0] + ue[1:]
print(ue_t)
hi_t = np.concatenate([hi[1:], si[0]])
mi_t = np.concatenate([ue[n-1], mi[1:]])
si_t = np.concatenate([si[1:], mi[n-1]])

print(ue_t)
A[0,:] = ue_t
A[:,0] = hi_t
A[:,n-1] = mi_t
A[n-1,:] = si_t

print(A)