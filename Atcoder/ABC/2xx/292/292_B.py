# https://atcoder.jp/contests/abc292/tasks/abc292_b

n, q = map(int, input().split())
player = [0]*n
for t in range(q):
    e, x = map(int, input().split())
    if e == 1:
        player[q] += 1
    if e == 2:
        player[q] += 2
    if e == 3:
        if player[q] >= 2:
            print('Yes')
        else:
            print('No')