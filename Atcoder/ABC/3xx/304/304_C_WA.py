# https://atcoder.jp/contests/abc304/tasks/abc304_c

import numpy as np
n, d = map(int, input().split())
list1 = []
iti = []
temp = 0
ini = 1
for t1 in range(n):
    if t1 == 0:
        list1.append('Yes')
    else:
        list1.append('No')
    temp1 , temp2 = map(int, input().split())
    iti.append(np.array([temp1,temp2]))
for t3 in range(n):
    if list1[t3] == 'Yes':
        for t in range(ini,n):
            #if list1[t] == 'No':
                dis=np.linalg.norm(iti[t3]-iti[t])
                if dis <= d:
                    list1[t] = 'Yes'
    ini += 1
    print(list1[t3])

# print(list1)