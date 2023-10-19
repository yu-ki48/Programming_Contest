# https://atcoder.jp/contests/abc308/tasks/abc308_b

n, m = map(int, input().split())
c = list(map(str, input().split()))
d = list(map(str, input().split()))
p = list(map(int, input().split()))
mydict = {}
sum = 0
for t in range(len(d)):
    mydict[d[t]] = p[t+1]

for t2 in c:
    if (t2 in mydict) == False:
        sum += p[0]
    elif t2 in mydict:
        sum += mydict[t2]

print(sum)