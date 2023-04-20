#不完全やで
n, k = map(int, input().split())
a = input()
a = a.split(' ')
sum = 0
max = 0
for temp1 in range(1, k+1):
    for temp2 in a:
        num = int(temp2)
        sum +=  (temp1 ^ num)
    if sum > max:
        max = sum
    sum = 0
print(max)