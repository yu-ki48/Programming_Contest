# https://atcoder.jp/contests/abc293/tasks/abc293_c

import itertools
h, w = map(int, input().split())
A = [list(map(int, input().split())) for i in range(h)]
yoko = [0]*(w-1)
tate = [1]*(h-1)
temp = set(itertools.permutations(yoko+tate))
counter = 0
for t1 in temp:
    x = y = 0
    temp2 = {A[x][y]}
    for t2 in t1:
        if t2 == 1:
            x += 1
            if A[x][y] not in temp2:
                temp2.add(A[x][y])
        elif t2 == 0:
            y += 1
            if A[x][y] not in temp2:
                temp2.add(A[x][y])
        else:
            break
    if (len(t1)+1) == len(temp2):
        counter += 1
print(counter)  
      