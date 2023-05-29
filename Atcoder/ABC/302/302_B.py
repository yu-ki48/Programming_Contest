# https://atcoder.jp/contests/abc302/tasks/abc302_b

import numpy as np
h, w = map(int, input().split())
s = np.array([list(input()) for i in range(h)])

for i in range(h):
    for j in range(w):
        if i > 3:
            if s[i][j] == 's' and s[i-1][j] == 'n' and s[i-2][j] == 'u' and s[i-3][j] == 'k' and s[i-4][j] == 'e':
                print(str(i+1) + ' ' + str(j+1))
                print(str(i) + ' ' + str(j+1))
                print(str(i-1) + ' ' + str(j+1))
                print(str(i-2) + ' ' + str(j+1))
                print(str(i-3) + ' ' + str(j+1))
        if i < h - 4:
            if s[i][j] == 's' and s[i+1][j] == 'n' and s[i+2][j] == 'u' and s[i+3][j] == 'k' and s[i+4][j] == 'e':
                print(str(i+1) + ' ' + str(j+1))
                print(str(i+2) + ' ' + str(j+1))
                print(str(i+3) + ' ' + str(j+1))
                print(str(i+4) + ' ' + str(j+1))
                print(str(i+5) + ' ' + str(j+1))
        if j < w - 4:
            if s[i][j] == 's' and s[i][j+1] == 'n' and s[i][j+2] == 'u' and s[i][j+3] == 'k' and s[i][j+4] == 'e':
                print(str(i+1) + ' ' + str(j+1))
                print(str(i+1) + ' ' + str(j+2))
                print(str(i+1) + ' ' + str(j+3))
                print(str(i+1) + ' ' + str(j+4))
                print(str(i+1) + ' ' + str(j+5))
        if j > 3:
            if s[i][j] == 's' and s[i][j-1] == 'n' and s[i][j-2] == 'u' and s[i][j-3] == 'k' and s[i][j-4] == 'e':
                print(str(i+1) + ' ' + str(j+1))
                print(str(i+1) + ' ' + str(j))
                print(str(i+1) + ' ' + str(j-1))
                print(str(i+1) + ' ' + str(j-2))
                print(str(i+1) + ' ' + str(j-3))
        if i < h - 4 and j < w - 4:
            if s[i][j] == 's' and s[i+1][j+1] == 'n' and s[i+2][j+2] == 'u' and s[i+3][j+3] == 'k' and s[i+4][j+4] == 'e':
                print(str(i+1) + ' ' + str(j+1))
                print(str(i+2) + ' ' + str(j+2))
                print(str(i+3) + ' ' + str(j+3))
                print(str(i+4) + ' ' + str(j+4))
                print(str(i+5) + ' ' + str(j+5))
        if i > 3 and j > 3:
            if s[i][j] == 's' and s[i-1][j-1] == 'n' and s[i-2][j-2] == 'u' and s[i-3][j-3] == 'k' and s[i-4][j-4] == 'e':
                print(str(i+1) + ' ' + str(j+1))
                print(str(i) + ' ' + str(j))
                print(str(i-1) + ' ' + str(j-1))
                print(str(i-2) + ' ' + str(j-2))
                print(str(i-3) + ' ' + str(j-3))
        if i < h - 4 and j > 3:
            if s[i][j] == 's' and s[i+1][j-1] == 'n' and s[i+2][j-2] == 'u' and s[i+3][j-3] == 'k' and s[i+4][j-4] == 'e':
                print(str(i+1) + ' ' + str(j+1))
                print(str(i+2) + ' ' + str(j))
                print(str(i+3) + ' ' + str(j-1))
                print(str(i+4) + ' ' + str(j-2))
                print(str(i+5) + ' ' + str(j-3))
        if i > 3 and j < w - 4:
            if s[i][j] == 's' and s[i-1][j+1] == 'n' and s[i-2][j+2] == 'u' and s[i-3][j+3] == 'k' and s[i-4][j+4] == 'e':
                print(str(i+1) + ' ' + str(j+1))
                print(str(i) + ' ' + str(j+2))
                print(str(i-1) + ' ' + str(j+3))
                print(str(i-2) + ' ' + str(j+4))
                print(str(i-3) + ' ' + str(j+5))