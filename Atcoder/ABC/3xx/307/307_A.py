# https://atcoder.jp/contests/abc307/tasks/abc307_a

n = int(input())
a = list(map(int, input().split()))
ans = []
ch = 0
sum = 0
for t1 in a:
    sum += t1
    ch += 1
    if ch == 7:
        ans.append(sum)
        ch = 0
        sum = 0
print(*ans)
