# https://atcoder.jp/contests/abc303/tasks/abc303_a

n = int(input())
s = list(map(str,input()))
t = list(map(str,input()))
ch = 0
for i in range(n):
    if s[i] == t[i] or (s[i] == 'l' and t[i] == '1' or s[i] == '1' and t[i] == 'l') or (s[i] == '0' and t[i] == 'o' or s[i] == 'o' and t[i] == '0'):
        ch += 0
    else:
        ch += 1
if ch == 0:
    print('Yes')
else:
    print('No')