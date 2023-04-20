# https://atcoder.jp/contests/typical90/tasks/typical90_bo

import numpy as np
def henkan(n):
  n1 = str(np.base_repr(n, 9))
  n1 = n1.replace('8', '5')
  return n1
n, k = map(int, input().split())
for t in range(k):
	n = str(n)
	n = '0o' + n
	n = int(n, 8)
	n = int(henkan(n))
print(n)