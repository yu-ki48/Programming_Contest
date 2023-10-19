# https://atcoder.jp/contests/abc296/tasks/abc296_a

def hantei(S):
    temp = ''
    for t in S:
        if temp == t:
            return 0
        temp = t
    return 1
n = input()
S = list(map(str, input().split()))
if hantei(S) == 1:
    print('Yes')
else:
    print('No')