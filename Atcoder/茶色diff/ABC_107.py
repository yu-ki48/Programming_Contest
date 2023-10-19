# https://atcoder.jp/contests/abc107/tasks/abc107_b

h, w = map(int, input().split())
A = []
gyou = set()
retu = set()
ans = []

for t in range(h):
  A.append(list(input()))

for i in range(h):
  for j in range(w):
    if A[i][j] == '#':
      gyou.add(i)
      retu.add(j)
ue = min(retu)
sita = max(retu)

gyou = list(gyou)
retu = list(retu)
gyou.sort()
retu.sort()

for t2 in gyou:
  for t3 in retu:
    print(A[t2][t3], end='')
  print()