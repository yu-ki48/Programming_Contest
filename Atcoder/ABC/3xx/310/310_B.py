# https://atcoder.jp/contests/abc310/tasks/abc310_b

n, m = map(int, input().split())
syouhin = []
ch = 0
for t in range(n):
    temp = list(map(int, input().split()))
    syouhin.append(temp)
def hantei(a,b):
    ch = 0
    for t1 in range(len(a)):
        if a[t1] in b:
            ch += 1
    if ch == len(a):
        return True
    else:
        return False

for i in range(n):
    for j in range(n):
        print(syouhin[i][2:])
        if ((syouhin[i][0] >= syouhin[j][0]) and hantei(syouhin[i][2:],syouhin[j][2:]) and ((syouhin[i][0] > syouhin[j][0]) or (len(syouhin[j][1]) > len(syouhin[i][1])))):
            ch += 1

if ch != 0:
    print('Yes')
else:
    print('No')