# https://atcoder.jp/contests/abc318/tasks/abc318_b

import numpy as np

n = int(input())

z = np.array([[0] * 100 for i in range(100)])

ans = 0

for i in range(n):
    a, b, c, d = map(int, input().split())
    z[a:b, c:d] += 1

for j in range(100):
    for k in range(100):
        if z[j,k] > 0:
            ans += 1
print(ans)