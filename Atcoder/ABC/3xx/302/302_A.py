# https://atcoder.jp/contests/abc302/tasks/abc302_a

a, b = map(int, input().split())
ch = 0
if a % b == 0:
    ch = a // b
else:
    ch = a // b + 1
print(ch)