sum1 = 0

for i in range(1, 101):
    if i % 2 != 0:
        continue
    sum1 += i
print('合計値は', sum1, 'です。')

sum2 = 0

for j in range(0, 102, 2):
    sum2 += j
print('合計値は', sum2, 'です。')

num = input('数字を入力してください：')
print('2倍すると...', float(num) * 2)

