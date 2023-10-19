# https://atcoder.jp/contests/abc320/tasks/abc320_b

s = input()

ans = 0
for i in range(len(s)):
  for j in range(1, len(s)-i+1):
    search = s[i:i+j]
    l = len(search)
    for k in range(l//2):
      if search[k] != search[l-k-1]:
        break
    else:
      ans = max(ans, l)
print(ans)