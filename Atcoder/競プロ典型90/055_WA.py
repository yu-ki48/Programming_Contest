# https://atcoder.jp/contests/typical90/tasks/typical90_bc
#未完成
import itertools as iter
import numpy as np
n, p, q = map(int, input().split())
A = list(map(int, input().split()))
#A = np.array(A)
counter = 0
for t in iter.combinations(A, 5):
    temp = np.prod(t)
    if temp % p == q:
        counter += 1
print(counter)
