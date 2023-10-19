# https://atcoder.jp/contests/abc314/tasks/abc314_c

n, m = map(int, input().split())

s = input()

C = list(map(int, input().split()))

color = [[] for i in range(m)]

ch = [0] * m

for i in range(n):
    color[C[i] - 1].append(i) 

for t in range(n):
  if ch[C[t] - 1] == 0:
    print(s[color[C[t] - 1][-1]], end='')
    ch[C[t] - 1] += 1
  else:
    print(s[color[C[t] - 1][ch[C[t] - 1]-1]], end='')
    ch[C[t] - 1] += 1
    