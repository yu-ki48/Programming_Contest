# https://atcoder.jp/contests/abc307/tasks/abc307_b

n = int(input())
s = []
for t in range(n):
    s.append(input())
ch = 0
for i in range(len(s)):
    for j in range(len(s)):
        if i != j:
            temp = s[i] + s[j]
            temp_r = list(temp)
            temp_r = reversed(temp_r)
            ''.join(temp_r)
            if temp == temp_r:
                ch = 1
                break
if ch == 1:
    print('Yes')
else:
    print('No')