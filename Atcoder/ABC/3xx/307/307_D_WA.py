# https://atcoder.jp/contests/abc307/tasks/abc307_d

n = int(input())
s = input()
s_r = list(s)
s_r = reversed(s_r)
s_r = ''.join(s_r)
l = s.find('(')
r = s_r.find(')')
temp = s_r[:r]
temp = list(temp)
temp = reversed(temp)
temp = ''.join(temp)
if r >= 0 and l >= 0:
    ans = s[:l] + temp
    print(ans)
else:
    print(s)