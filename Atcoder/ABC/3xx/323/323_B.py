# https://atcoder.jp/contests/abc323/tasks/abc323_b

n = int(input())
player = []
for t in range(n):
    s = input()
    num = s.count('o')
    player.append((num,t+1))

player.sort(key=lambda x:x[0],reverse=True)

for t2 in range(n):
    print(player[t2][1], end=' ')