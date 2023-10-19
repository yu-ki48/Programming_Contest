# https://atcoder.jp/contests/abc281/tasks/abc281_c

temp1 = input()
temp2 = input()
num = temp1.split(' ')
sog = temp2.split(' ')
i = 0
sum = 0
while True:
    tem = sog[i]
    sum += int(tem)
    i += 1
    if int(num[1]) < sum:
        print(i, end = ' ')
        print(int(tem) - (sum - int(num[1])))
        break
    if i == int(num[0]) + 1:
        i = 0