# https://atcoder.jp/contests/abc312/tasks/abc312_b

import numpy as np

n, m = map(int, input().split())
s = np.array([list(input()) for i in range(n)])
np.place(s, s == '.', 0)
np.place(s, s == '#', 1)
s = np.asarray(s, dtype = int)
s = np.pad(s, 1, "constant")
print(s)
ch1 = [[1,1,1,0],
      [1,1,1,0],
      [1,1,1,0],
      [0,0,0,0]]

ch2 = [[0,0,0,0],
      [0,1,1,1],
      [0,1,1,1],
      [0,1,1,1]]

for i in range(n):
    for j in range(m):
        if np.array_equal(s[i+1:i+1+5,j+1:j+1+5],ch1) and np.array_equal(s[i+6:i+10, j+6:j+10],ch2):
            print(i+1, j+1)