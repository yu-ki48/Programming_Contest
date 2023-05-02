# https://atcoder.jp/contests/abc300/tasks/abc300_a

n, a, b = map(int, input().split())
c = list(map(int, input().split()))
ans = a + b
for i in range(n):
    if c[i] == ans:
        print(i+1)
