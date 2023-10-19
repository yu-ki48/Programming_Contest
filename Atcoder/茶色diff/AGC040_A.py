# https://atcoder.jp/contests/agc040/tasks/agc040_a

s = list(input())
a = [0] * (len(s) + 1)

for i in range(len(s)):
    if s[i] == '<':
        a[i+1] = max(a[i+1], a[i]+1)

for j in range(len(s)-1, -1, -1):
    if s[j] == '>':
        a[j] = max(a[j], a[j+1]+1)

print(sum(a))
    