# https://atcoder.jp/contests/abc294/tasks/abc294_a

n = int(input())
A = list(map(int, input().split()))
B = []
for t in A:
    if t % 2 == 0:
        B.append(t)
print(*B)