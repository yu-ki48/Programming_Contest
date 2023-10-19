# https://atcoder.jp/contests/abc154/tasks/abc154_d

n, k = map(int, input().split())

p = list(map(int, input().split()))

kitaitis = [-1] * 1000

def keisan(m):
    sum_t = 0 
    for i in range(1,m+1):
        sum_t += i
    kitaitis[m-1] = sum_t / m
    return kitaitis[m-1]

max_sum = 0
for l in range(10 - (k + 1)):
    bubun_sum = sum(p[l:l+k+1])
    if max_sum < bubun_sum:
        max_sum = bubun_sum
        ind = l

ans = 0

for j in range(k):
    if kitaitis[p[l+j] - 1] == -1:
        ans += float(keisan(p[l+j]))
    else:
        ans += float(kitaitis[p[l+j] - 1])
print('{:.10f}'.format(ans))