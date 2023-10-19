# https://atcoder.jp/contests/abc323/tasks/abc323_a

s = list(input())
def hantei(s):
    for t in range(1, len(s), 2):
        if s[t] != '0':
            return False
    return True

if hantei(s) == True:
    print('Yes')
else:
    print('No')