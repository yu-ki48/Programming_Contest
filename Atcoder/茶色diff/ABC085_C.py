# https://atcoder.jp/contests/abc085/tasks/abc085_c

n, y = map(int, input().split())

def hantei(n,y):
  man = y // 10000
  go = y // 5000
  for k in range(man+1):
    for j in range(go+1):
      i = n - (k + j)
      if i >= 0:
        goukei = (1000 * i) + (5000 * j) + (10000 * k)
        if (goukei == y) and (n == (i + j + k)):
          return (k, j, i)
  return False

kekka = hantei(n,y)

if kekka != False:
  print(*kekka)
else:
  print(-1,-1,-1)