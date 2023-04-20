# https://atcoder.jp/contests/typical90/tasks/typical90_bi

q = int(input())
list1 = []
for temp in range(q):
    t, x = map(int, input().split())
    if t == 1:
        list1 = [x] + list1
    elif t == 2:
        list1 = list1 + [x]
    else:
        print(list1[x-1])

