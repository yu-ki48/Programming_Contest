# https://atcoder.jp/contests/abc300/tasks/abc300_c

import numpy as np
h, w = map(int, input().split())
def batu(n):
    cross = np.zeros((n,n), dtype=str)
    for t in range(n):
        for s in range(n):
            if t+s == n-1 or t == s:
                cross[t,s] = '#'
            else:
                cross[t,s] = '.'
    return cross

c = np.array([list(input()) for i in range(h)])
n = min(h,w)
if n % 2 == 0:
    n -= 1
ind = 0
ans = [0] * n
for i in range(n,2,-2):
    temp = batu(i)
    for j in range(h-i+1):
        for k in range(w-i+1):
            if np.array_equal(c[j:j+i,k:k+i],temp):
                ans[ind] += 1
                c[j:j+i,k:k+i] = 0
                print(c)
    ind += 1
print(*ans)