# https://atcoder.jp/contests/abc300/tasks/abc300_b

import numpy as np
def hantei(A,B, h, w):
    A_tile = np.tile(A, (2, 2))
    for i in range(h):
        for j in range(w):
            if np.array_equal(A_tile[i:i+h,j:j+w],B):
                return 1
    return 0
h, w = map(int, input().split())
A = np.array([list(input()) for i in range(h)])
B = np.array([list(input()) for i in range(h)])
if hantei(A,B,h,w) == 1:
    print('Yes')
else:
    print('No')