x, a, b, c = map(float, input().split())
if (x / a + c) > x / b:
    print('Tortoise')
elif (x / a + c) == x / b:
    print('Tie')
else:
    print('Hare')