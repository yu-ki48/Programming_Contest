# https://atcoder.jp/contests/abc319/tasks/abc319_d

n, m = map(int, input().split())

L = list(map(int, input().split()))

for k in range(n):
  L[k] += 1

L_sum = sum(L)

lower = max(L) - 1
upper = L_sum

while (lower + 1 < upper):
  middle = (lower + upper) // 2

  c = 1
  hasi = 0
  for i in range(n):
    hasi += L[i]
    if hasi > middle: 
      c += 1
      hasi = L[i]
  if c > m:
    lower = middle
  else:
    upper = middle
print(upper - 1)
