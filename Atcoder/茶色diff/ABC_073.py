# https://atcoder.jp/contests/abc073/tasks/abc073_c

n = int(input())
temp = []
res = 0
t = 0

for i in range(n):
    temp.append(int(input()))

temp.sort()

while t < n:
    cc = temp[t]
    f = 0
    while (t < n) and (cc == temp[t]):
        f += 1
        t += 1
    res += (f % 2)
print(res)