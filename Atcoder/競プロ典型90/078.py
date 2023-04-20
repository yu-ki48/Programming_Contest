# https://atcoder.jp/contests/typical90/tasks/typical90_bz

n, m = map(int, input().split())
list1 = [0]*n
for t in range(m):
    a, b = map(int, input().split())
    if a > b:
        list1[a-1] += 1
    else:
        list1[b-1] += 1
print(list1.count(1))