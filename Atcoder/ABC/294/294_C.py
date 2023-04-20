# https://atcoder.jp/contests/abc294/tasks/abc294_c

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = A + [10000000000]
B = B + [10000000000]
Akai = []
Bkai = []
for t in range(n+m):
    if A[0] < B[0]:
        Akai.append(t+1)
        A.pop(0)
    else:
        Bkai.append(t+1)
        B.pop(0)
print(*Akai)
print(*Bkai)