# https://atcoder.jp/contests/abc305/tasks/abc305_d

n = int(input())
a = list(map(int, input().split()))
neta = []
data = [0] * (a[-1] + 1)
#print(len(data))
for temp in range(1,len(a)):
    if temp %2 == 0:
	    neta.append((a[temp-1],a[temp]))
#print(neta)
for temp2 in range(len(data)):
    for temp3 in neta:
        if temp3[0] <= temp2-1 and temp2 <= temp3[1]:
            data[temp2] = 1

for temp4 in range(1,len(data)):
    data[temp4] += data[temp4-1] 
#print(data[-1]) 
q = int(input())
for t in range(q):
    ans = 0
    r, l = map(int, input().split())
    ans = data[l] - data[r]
    print(ans)