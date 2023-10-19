# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_g

n, x, y = map(int, input().split())
ans = 0
seki = x * y
for t in range(1, n + 1):
  if t % x == 0 or t % y == 0:
    ans += 1
print(ans)
