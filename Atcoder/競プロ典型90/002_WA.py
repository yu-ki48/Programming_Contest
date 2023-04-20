# https://atcoder.jp/contests/typical90/tasks/typical90_b

def hantei(s):
    dep = 0
    for temp in s:
        if temp == '(':
            dep += 1
        if temp == ')':
            dep -= 1
        if dep < 0:
            return False
    if dep == 0:
        return True
    return False

n = int(input())
i = 0
j = n - 1 
while i < 1 << n:
    list1 = []
    while j >= 0:
        if i & (1 << j) == 0:
            list1.append('(')
        else:
            list1.append(')') 
        j -= 1
    i += 1
if hantei(list1) == True:
    print(list1)
    

