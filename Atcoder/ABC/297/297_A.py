# https://atcoder.jp/contests/abc297/tasks/abc297_a

def check(T):
    for t in range(1, n):
        if T[t] - T[t-1] <= d:
            return t
n, d = map(int, input().split())
T = list(map(int, input().split()))
t = check(T)
if t == None:
    print(-1)
else:
    print(T[t])

