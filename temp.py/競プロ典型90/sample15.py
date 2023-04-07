n = int(input())
i = 0
list1 = []
list2 = []
class1 = 0
class2 = 0
for t in range(n):
    c, p = map(int, input().split())
    if c == 1:
       class1 += p
    else:
       class2 += p
    list1.append((p))
tuple1 = tuple(list1)
q = int(input())
j = 0
for s in range(q):
    class1 = 0
    class2 = 0
    l, r = map(int, input().split())
    temp1 = tuple1[l-1:r]
    for temp in temp1:
      if temp[0] == 1:
        class1 += temp[1]
      else:
        class2 += temp[1]
    print(str(class1) + ' ' + str(class2))