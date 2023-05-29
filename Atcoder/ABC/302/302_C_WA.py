# https://atcoder.jp/contests/abc302/tasks/abc302_c

import numpy as np
n, m = map(int, input().split())
s = np.array([list(input()) for i in range(n)])
temp2 = []
temp = 1
for i in range(n):
    for j in range(temp,n):
        diff_list = set(s[i]) ^ set(s[j])
        if len(diff_list) == 1:
            print(diff_list)
            temp2.append(i)
            temp2.append(j)
            temp += 1
print(temp2)
set1 = set(temp2)
if len(set1) == n-1:
    print('Yes')
else:
    print('No')