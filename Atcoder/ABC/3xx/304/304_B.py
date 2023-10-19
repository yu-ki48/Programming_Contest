# https://atcoder.jp/contests/abc304/tasks/abc304_b

n = int(input())
n_t = str(n)
nagasa = len(n_t)
ans = []
if nagasa > 3:
    nagasa = len(n_t) - 3
for t in range(n_t):
    if t < 3:
        ans.append(n_t[t])
    else:
        ans.append('0')
ans = int(ans)
print(ans)