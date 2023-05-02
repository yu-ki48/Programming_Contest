# https://atcoder.jp/contests/abc299/tasks/abc299_b

n, T = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))
ind = 0
max = 0
if T in c:
    temp = [i for i, x in enumerate(c) if x == T]
else:
    temp = [i for i, x in enumerate(c) if x == c[0]]
for t in temp:
    if r[t] > max:
        max = r[t]
print(r.index(max) + 1)

