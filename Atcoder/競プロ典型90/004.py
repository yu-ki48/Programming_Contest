# https://atcoder.jp/contests/typical90/tasks/typical90_d

import numpy as np
h, w = map(int, input().split())
A = [list(map(int, input().split())) for i in range(h)]
A = np.array(A)
B = -A
for yoko in range(h):
    B[yoko, :] += sum(A[yoko, :])

for tate in range(w):
    B[:, tate] += sum(A[:, tate])

for i in range(h):
    print(*B[i])