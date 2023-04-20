# https://atcoder.jp/contests/abc294/tasks/abc294_b

h, w = map(int, input().split())
A = [list(map(int, input().split())) for i in range(h)]
x = y = 0
B = []
 
for t1 in range(h):
    for t2 in range(w):
        if A[t1][t2] == 0:
            print('.', end='')
        else:
            print(chr(64+A[t1][t2]), end='')
    print('')