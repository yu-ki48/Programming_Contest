# https://atcoder.jp/contests/abc290/tasks/abc290_c

n, k = map(int, input().split())
a = input()
a = a.split(' ')
a = [int(s) for s in a]
b = sorted(a)
ch = 0
i = 0
while ch == b[i] and ch != k:
    i += 1
    if b[i] > ch:
        ch += 1
print(ch)

