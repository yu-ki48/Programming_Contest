sum = 0
temp1 = input()
temp3 = temp1.split(' ')
indN = int(temp3[0])
indM = int(temp3[1])
A = input()
score = A.split(' ')
B = input()
temp2 = B.split(' ')
for temp in temp2:
    sum += int(score[int(temp) - 1])
print(sum)

