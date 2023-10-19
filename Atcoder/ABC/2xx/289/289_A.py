# https://atcoder.jp/contests/abc289/tasks/abc289_a

s = list(str(input()))
for t in range(len(s)):
    if s[t] == '1':
        s[t] = '0'
    else:
        s[t] = '1'

print(''.join(s))

    