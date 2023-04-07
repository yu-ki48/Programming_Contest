#未完成です
import math
n1 = int(input())
n2 = math.ceil(n1 / 2)
goukei = 0
def counter(num):
    count = 0
    num1 = math.sqrt(num)
    num2 = int(num1)
    for t in range(1, num2 + 1):
        if num % t == 0:
            count += 1
    if num % num1 == 0:
        return count * 2 - 1
    else:
    	return count *2

for temp in range(1, n2):
    temp1 = 0
    temp2 = 0
    temp1 += counter(temp)
    temp2 += counter(n1 - temp)
    goukei  += temp1 * temp2
print(goukei * 2)