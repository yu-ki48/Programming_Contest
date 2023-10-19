# https://atcoder.jp/contests/abc321/tasks/abc321_a

n = list(str(input()))

def hantei(n):
  for i in range(len(n) - 1):
      if n[i+1] >= n[i]:
          return -1
  return 1

if hantei(n) == 1:
  print('Yes')
else:
  print('No')
