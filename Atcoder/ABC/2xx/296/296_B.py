# https://atcoder.jp/contests/abc296/tasks/abc296_b

def hantei(S):
    for t in range(len(S)):
        if S[t] == '*':
            return chr(97 + t)

for temp in reversed(range(1,9)):
    S = input()
    if hantei(S) != None:
        print(hantei(S), end='')
        print(temp)