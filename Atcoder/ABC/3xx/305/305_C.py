# https://atcoder.jp/contests/abc305/tasks/abc305_c

import numpy as np
h, w = map(int, input().split())
s = np.array([list(input()) for i in range(h)])
s = np.pad(s, 1, "constant")
ch = 0
for i in range(h+1):
    for j in range(w+1):
        ch = 0
        if s[i,j] == '.':
            if s[i-1,j] == '#':
                ch += 1
            if s[i+1,j] == '#':
                ch += 1
            if s[i,j-1] == '#':
                ch += 1
            if s[i,j+1] == '#':
                ch += 1
        if ch >= 2:
            print(i, j)