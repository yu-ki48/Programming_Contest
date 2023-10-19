# https://atcoder.jp/contests/abc314/tasks/abc314_b

n = int(input())

player = []

for t in range(n):
    c = int(input())
    A = list(map(int, input().split()))
    player.append((c,A))

ans = []

x = int(input())
for i in range(n):
  if x in player[i][1]:
    ans.append((i+1, player[i][0]))
if len(ans) == 0:
  print(0)
else:

  ans.sort(key=lambda x:x[1])
  
  min_num = ans[0][1]
  temp = []
  for j in range(len(ans)):
    if min_num == ans[j][1]:
      temp.append(ans[j][0])
  print(len(temp))
  print(*temp)