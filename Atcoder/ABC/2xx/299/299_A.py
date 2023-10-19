# https://atcoder.jp/contests/abc299/tasks/abc299_a

def hantei(s):
    ch = 0
    for t in s:
        if '*' == t:
            return ch
        if '|' == t:
            ch += 1
n = input()
s = input()
if hantei(s) == 1:
    print('in')
else:
    print('out')