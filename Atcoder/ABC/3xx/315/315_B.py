# https://atcoder.jp/contests/abc315/tasks/abc315_b

m = int(input())

d = list(map(int, input().split()))

d_sum = (sum(d) - 1)

mid = (d_sum // 2) + 1

ans = 0
day = 0
for i in range(m):
    if (ans + d[i]) >= mid:
        day = mid - ans
        print(i+1, day)
        break
    ans += d[i]