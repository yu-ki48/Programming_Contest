# https://atcoder.jp/contests/abc304/tasks/abc304_c

import numpy as np
n, d = map(int, input().split())
list2 = np.zeros((n,n))
list1 = []
iti = []
for t1 in range(n):
    if t1 == 0:
        list1.append('Yes')
    else:
        list1.append('No')
    temp1 , temp2 = map(int, input().split())
    iti.append(np.array([temp1,temp2]))

for h in range(n):
    for w in range(n):
        if w >= 1 and w - h >= 1:
            list2[h,w] = np.linalg.norm(iti[h]-iti[w])

for t in range(n-1):
    if min(list2[t,t+1:]) <= d:
        print('Yes')
    else:
        print('No')
