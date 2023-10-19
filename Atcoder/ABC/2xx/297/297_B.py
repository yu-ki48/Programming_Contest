# https://atcoder.jp/contests/abc297/tasks/abc297_b

S = input()
ch = 0
temp1 = S.find('B')
temp2 = S[temp1+1:].find('B') + temp1 + 1
if (temp1 % 2) != (temp2 % 2):
    ch += 1
temp3 = S.find('R')
temp4 = S[temp3+1:].find('R') + temp3 + 1
temp5 = S.find('K')
if temp3 < temp5 and temp5 < temp4:
    ch += 1
if ch == 2:
    print('Yes')
else:
    print('No')