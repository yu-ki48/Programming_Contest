# https://atcoder.jp/contests/abc303/tasks/abc303_b

from scipy.special import comb
n, m = map(int, input().split())
temp = comb(n, 2, exact=True)
set1 = set()
for t in range(m):
    a = list(map(int,input().split()))
    for i in range(n-1):
        if a[i] < a[i+1]:
            set1.add((a[i], a[i+1]))
        else:
        	set1.add((a[i+1], a[i]))
print(temp - len(set1))