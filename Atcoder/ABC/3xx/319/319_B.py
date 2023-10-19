# https://atcoder.jp/contests/abc319/tasks/abc319_b

n = int(input())

yaku = []
for t in range(9):
    if n % (t+1) == 0:
        yaku.append(t+1)
for i in range(n+1):
    flag = False
    for j in yaku:
        if i % (n // j) == 0:
            print(j, end='')
            flag = True
            break
    if flag == False:
        print('-')     