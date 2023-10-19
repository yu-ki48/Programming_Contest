# https://atcoder.jp/contests/abc293/tasks/abc293_a

s = list(input())
temp = len(s)
for t in range(temp // 2):
    temp1 = s[2 * t]
    s[2 * t] = s[2 * t + 1]
    s[2 * t + 1] = temp1
print(''.join(s))
