# https://atcoder.jp/contests/practice2/tasks/practice2_a

n, q = map(int, input().split())
log = []
for t in range(q):
    t, u, v = map(int, input().split())
    if t == 0:
        log.append((u,v))
    else:
        if (u,v) in log == True:
            print(1)
        else:
            print(0)
