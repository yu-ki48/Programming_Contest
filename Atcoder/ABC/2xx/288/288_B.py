# https://atcoder.jp/contests/abc288/tasks/abc288_b

n, k = map(int, input().split())
s = []
for _ in range(n):
    s.append(input())
s = s[:k]
s.sort()
for t in range(k):
    print(s[t])
