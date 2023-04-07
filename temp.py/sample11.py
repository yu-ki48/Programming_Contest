#def has_duplicates2(seq):
#    seen = []
#    unique_list = [x for x in seq if x not in seen and not seen.append(x)]
#    return len(seq) != len(unique_list)
def check(list1,s):
    x = 0
    y = 0
    for temp in s:
        if temp == 'R':
            x += 1
            list1.append([x,y])
        if temp == 'L':
            x -= 1
            list1.append([x,y])
        if temp == 'U':
            y += 1
            list1.append([x,y])
        if temp == 'D':
            y -= 1
            list1.append([x,y])
        if [x,y] in list1[:-1]:
            return 1

n = int(input())
s = input()
list1 = [[0,0]]
if check(list1,s) == 1:
    print('Yes')
else:
    print('No')
