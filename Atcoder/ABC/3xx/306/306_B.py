# https://atcoder.jp/contests/abc306/tasks/abc306_b

a = list(map(int, input().split()))
sum = 0
for t in range(len(a)):
    if a[t] == 1:
        sum += (1 << t)
print(sum)