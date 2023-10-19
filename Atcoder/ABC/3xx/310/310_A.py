# https://atcoder.jp/contests/abc310/tasks/abc310_a

n, p, q = map(int, input().split())
d = list(map(int, input().split()))
m = min(d)
if p < (q + m):
    print(p)
else:
    print(q + m)
