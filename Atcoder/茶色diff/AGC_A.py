# https://atcoder.jp/contests/agc029/tasks/agc029_a

s = input()
ans = 0
front = 0
for t in range(len(s)):
    if s[t] == 'W':
        ans += (t - front)
        front += 1

print(ans)