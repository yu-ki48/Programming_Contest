# https://atcoder.jp/contests/abc171/tasks/abc171_c

n = int(input())
syou = -1
amari = []
while syou != 0:
    n -= 1
    syou = n // 26
    amari.append(n % 26)
    n = syou
amari.reverse()
for t in amari:
    print(chr(97 + t), end='')