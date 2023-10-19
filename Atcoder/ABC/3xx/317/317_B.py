# https://atcoder.jp/contests/abc317/tasks/abc317_b

n = int(input())

A = list(map(int, input().split()))

A.sort()

for i in range(n-1):
    if A[i] + 1 != A[i+1]:
        print(A[i+1]-1)
        break