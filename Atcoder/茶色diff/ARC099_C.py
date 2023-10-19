# https://atcoder.jp/contests/arc099/tasks/arc099_a

n, k = map(int, input().split())
A = list(map(int, input().split()))

min_a = min(A)
min_num = A.count(min_a)

if ((n - min_num) % (k - 1)) == 0:
    print((n - min_num) // (k - 1))
else:
    print((n - min_num) // (k - 1) + 1)
