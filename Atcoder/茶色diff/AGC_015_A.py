# https://atcoder.jp/contests/agc015/tasks/agc015_a

n, a, b = map(int,input().split())

max_sum = a + (b * (n-1))
min_sum = b + (a * (n-1))

if max_sum < min_sum:
  print(0)
else:
  print(max_sum - min_sum + 1)