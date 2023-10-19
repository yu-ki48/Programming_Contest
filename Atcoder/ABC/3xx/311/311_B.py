# https://atcoder.jp/contests/abc311/tasks/abc311_b

import numpy as np
n, d = map(int, input().split())

A = np.array([list(input()) for i in range(n)])
max_m = 0
ch = 0
for t in range(d):
    if 'x' not in A[:,t]:
        ch += 1
    if max_m < ch:
        max_m = ch
    if 'x' in A[:,t]:
        ch = 0

print(max_m)