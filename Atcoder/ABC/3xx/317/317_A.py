# https://atcoder.jp/contests/abc317/tasks/abc317_a

n, h, x = map(int, input().split())

P = list(map(int, input().split()))

for t in range(len(P)):
    if (x - h) <= P[t]:
        print(t+1)
        break