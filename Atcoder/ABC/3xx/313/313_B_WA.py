# https://atcoder.jp/contests/abc313/tasks/abc313_b

n, m = map(int, input().split())
temp1 = []
temp2 = []
for t in range(m):
    i, j = map(int, input().split())
    temp1.append(i)
    temp2.append(j)
temp1 = set(temp1)
temp2 = set(temp2)
if n > 2:
    if (len(temp1) == n-1) and (len(temp2) == n-1) and (temp1 != temp2):
        for t2 in range(1,n+1):
            if t2 not in temp2:
                print(t2)
    else:
        print(-1)
else:
    if m == 1:
        print(temp1[0])
    else:
        print(-1)
