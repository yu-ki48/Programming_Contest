# https://atcoder.jp/contests/abc309/tasks/abc309_c

n, k = map(int, input().split())
med = []
ch = 0
for t in range(n):
    a, b = map(int, input().split())
    med.append((a,b))
    ch += b
med.sort()
ind = 0
if ch <= k:
    print(1)
else:
    while ch > k:
        ch -= med[ind][1]
        ind += 1
    print(med[ind-1][0]+1)
