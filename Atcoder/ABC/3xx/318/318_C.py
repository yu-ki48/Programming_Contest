# https://atcoder.jp/contests/abc318/tasks/abc318_c

n, d, p = map(int, input().split())

F = list(map(int, input().split()))

F = sorted(F, reverse=True)


while len(F) %  d != 0:
    F.append(0)

sum_list = []

for i in range(len(F) // d):
    sum_list.append(sum(F[(i*d):((i+1)*d)]))

goukei = 0
for t in sum_list:
    if t > p:
        goukei += p
    else:
        goukei += t
print(goukei)
