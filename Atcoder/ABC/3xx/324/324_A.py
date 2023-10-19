# https://atcoder.jp/contests/abc324/tasks/abc324_a

n = int(input())
A = set(map(int, input().split()))

if len(A) == 1:
    print('Yes')
else:
    print('No')