# https://atcoder.jp/contests/abc322/tasks/abc322_b

n, m = map(int, input().split())

s = input()
t = input()

if s == t[:n] and s == t[-n:]:
    print(0)
elif s == t[:n]:
    print(1)
elif s == t[-n:]:
    print(2)
else:
    print(3)