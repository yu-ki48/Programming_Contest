# https://atcoder.jp/contests/abc157/tasks/abc157_c

n, m = map(int, input().split())
temp2 = set()
ch = [False] * n
ans = [0] * n

for t in range(m):
  keta, kazu = map(int, input().split()) 
  temp2.add((keta-1,kazu))

temp2 = list(temp2)

def hantei(temp):
  for t2 in range(len(temp)):
    if ch[temp[t2][0]] == False:
      ans[temp[t2][0]] = temp[t2][1]
      ch[temp[t2][0]] = True
    else:
      return True
  if (ans[0] == 0 and ch[0] == True)  and len(ans) > 1:    
    return True
  elif (ans[0] == 0 and ch[0] == True)  and len(ans) == 1:
    return ans
  else:
    if ch[0] == False:
      if len(ans) == 1:
        ans[0] = 0
      else:
        ans[0] = 1
    for t4 in range(1,n):
      if ch[t4] == False:
        ans[t4] = 0 
    return ans
    
if hantei(temp2) == True:
  print(-1)
else:
  for t3 in range(len(ans)):
    print(int(ans[t3]), end='')