# https://atcoder.jp/contests/abc306/tasks/abc306_a

n = int(input())
s = input()
ans = []
for t in range(n):
    for t1 in range(2):
        ans.append(s[t])
print(''.join(ans))
