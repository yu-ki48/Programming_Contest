# https://atcoder.jp/contests/abc301/tasks/abc301_a

t_win = 0
a_win = 0
n = int(input())
s = input()
if n % 2 == 0:
    boder = n // 2
else:
    boder = n // 2 + 1

for t in s:
    if t == 'T':
        t_win += 1
    if t == 'A':
        a_win += 1
    if boder == t_win:
        print('T')
        break 
    elif boder == a_win:
        print('A')
        break