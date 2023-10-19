# https://atcoder.jp/contests/abc312/tasks/abc312_c

import numpy as np

n, m = map(int, input().split())
a = np.array(list(map(int, input().split())))
b = np.array(list(map(int, input().split())))
a_s = np.sort(a)
b_s = np.sort(b)[::-1]
ch = 0
for j in range(m):
    counter = 0
    if a_s[-1] >= b_s[0]:
        counter = 0
        ch = 1
        break
    for i in range(n):
        if a_s[i] < b[j]:
            counter += 1 
        if i+1 > counter:
            print(a_s[i])
            ch = 1
            break
        if a_s[i] > b[j]:
            break 
    if ch == 1:
        counter = 1
        break
if counter == 0:
    print(b_s[0]+1)