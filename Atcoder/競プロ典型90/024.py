# https://atcoder.jp/contests/typical90/tasks/typical90_x

n, k = map(int, input().split())
dif_sum = 0
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for t in range(n):
    dif_sum += abs(A[t] - B[t])
temp = k - dif_sum
if temp >= 0 and temp % 2 == 0:
    print('Yes')
else:
    print('No')
