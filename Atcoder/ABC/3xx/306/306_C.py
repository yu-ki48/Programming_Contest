# https://atcoder.jp/contests/abc306/tasks/abc306_c
n = int(input())
a = list(map(int, input().split()))
counter = [0] * n 
ans = []
for t in a:
    if counter[t-1] == 1:
        ans.append(t)
    counter[t-1] += 1
    if len(ans) == n:
        break
print(*ans)