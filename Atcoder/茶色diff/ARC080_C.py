# https://atcoder.jp/contests/arc080/tasks/arc080_a

n = int(input())

ch_2 = 0
ch_4 = 0

a = list(map(int, input().split()))

for t in a:
    if t % 4 == 0:
        ch_4 += 1
    elif t % 2 == 0:
        ch_2 += 1
    

if ((ch_2 // 2) + ch_4) >= (n // 2):
    print('Yes')
else:
    print('No')
