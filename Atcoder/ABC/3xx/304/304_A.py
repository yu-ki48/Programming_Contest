# https://atcoder.jp/contests/abc304/tasks/abc304_a

n = int(input())
list1 = []
list2 = []
for t in range(n):
    name, a = map(str, input().split())
    list1.append(name)
    list2.append(int(a))

min_age = list2.index(min(list2))
print(min_age)
for t2 in range(n):
    print(list1[(min_age+t2)%n])
