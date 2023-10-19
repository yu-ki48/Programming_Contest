# https://atcoder.jp/contests/abc308/tasks/abc308_a

s = list(map(int, input().split()))
ch = 0
s_s = sorted(s)
if s != s_s:
    ch -= 1
for t in s:
    if t < 100 or 675 < t:
        ch -= 1
    if t % 25 != 0:
        ch -= 1

if ch > 0:
    print('Yes')
else:
    print('No')