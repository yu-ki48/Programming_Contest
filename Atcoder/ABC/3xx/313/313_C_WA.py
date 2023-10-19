# https://atcoder.jp/contests/abc313/tasks/abc313_c

n = int(input())
a = list(map(int, input().split()))
ave = sum(a) // len(a)
ans1 = 0
ans2 = 0
for t in a:
    if t <= ave:
        ans1 += (ave - t)
for t2 in a:
    if t2 >= ave:
        ans2 += (ave - t2)

if ans2 > ans1:
    print(ans2)
else:
    print(ans1)
