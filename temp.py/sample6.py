n, m = map(int, input().split())
s = input()
win = 0
list1 = []
for temp in s:
    if temp == 'o' and win < m:
        win += 1
        list1.append(temp)
    else:
        list1.append('x')
print(''.join(list1))