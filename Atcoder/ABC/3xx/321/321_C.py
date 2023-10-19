# https://atcoder.jp/contests/abc321/tasks/abc321_c

k = int(input())

ans = []

for i in range(2, 1 << 10):
    x = 0
    for j in range(9,-1,-1):
        if i & (1 << j):
            x *= 10
            x += j
    ans.append(x)
        
ans.sort()
print(ans[k-1])
