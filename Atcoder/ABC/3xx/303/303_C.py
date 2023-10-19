# https://atcoder.jp/contests/abc303/tasks/abc303_c

n, m, h, k = map(int, input().split())
s = input()
hil = set()
for i in range(m):
    hil.add(tuple(map(int, input().split())))

def hantei(hil,h,k,s):
    x = y = 0
    for t in s:
        if t == 'R':
            x += 1
            h -= 1
        if t == 'L':
            x -= 1
            h -= 1
        if t == 'U':
            y += 1
            h -= 1
        if t == 'D':
            y -= 1
            h -= 1
        if h < 0:
            return print('No')
        if (x,y) in hil and h <= k:
            h = k
            hil.remove((x,y))
    return print('Yes')

if h > n:
    print('Yes')
else:
    hantei(hil,h,k,s)