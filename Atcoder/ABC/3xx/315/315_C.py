# https://atcoder.jp/contests/abc315/tasks/abc315_c

n = int(input())

aice = []
ch = [0] * n

for t in range(n):
    f, s = map(int, input().split())
    aice.append([f,s])
aice.sort(key=lambda x:x[1],reverse=True)
    
for t2 in range(n):
    if ch[aice[t2][0]-1] != 0:
        aice[t2][1] = aice[t2][1] // 2
    ch[aice[t2][0]-1] += 1

aice.sort(key=lambda x:x[1],reverse=True)


print(aice[0][1] + aice[1][1])