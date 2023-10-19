# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_g

import math
n, x, y = map(int, input().split())
ans = 0
ans += n // x 
ans += n // y
ans -= n // ((x*y) // math.gcd(x,y))
print(ans)