n = int(input())
1 << n
print(1 << n)



import math
a, b, c = map(int, input().split())
gcd = math.gcd(math.gcd(a, b), c)
gcd = int(gcd)
#print(gcd)
temp1 = -1 + a // gcd
temp2 = -1 + b // gcd
temp3 = -1 + c // gcd
if gcd == 1:
  print(-3 + a + b + c)
else:
  print(temp1 + temp2 + temp3)
