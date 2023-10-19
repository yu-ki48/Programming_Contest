# https://atcoder.jp/contests/abc322/tasks/abc322_c

n, m = map(int, input().split())

A = list(map(int, input().split()))

ind = 0
for i in range(n):
    print(A[ind] - (i+1))
    if (i + 1) == A[ind]: 
        ind += 1
