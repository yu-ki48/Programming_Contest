# https://atcoder.jp/contests/abc291/tasks/abc291_c

def check(set1,s):
    x = 0
    y = 0
    for temp in s:
        if temp == 'R':
            x += 1
        if temp == 'L':
            x -= 1
        if temp == 'U':
            y += 1
        if temp == 'D':
            y -= 1
        if (x,y) in set1:
            return 1
        set1.add((x,y))

n = int(input())
s = input()
set1 = {(0,0)}

if check(set1,s) == 1:
    print('Yes')
else:
    print('No')