# https://atcoder.jp/contests/abc289/tasks/abc289_b

import numpy as np
n, m = map(int, input().split())
a = np.array(list(map(int, input().split())))
ans = np.arange(1,n+1)
temp = []
st = 0
flag= 0
for t1 in range(st, m):
    temp.append(ans[t1])
    for t2 in range(st + 1,m):
        if a[t2] - a[t1] == 1:
            temp.append(a[t2])
            flag = t2
    ans[st:st+a[flag]-1] = np.flipud(ans[st:st+a[flag]-1])
    st += len(temp)
    


print(ans) 
