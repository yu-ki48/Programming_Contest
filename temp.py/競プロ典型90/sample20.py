#競プロ典型90 No.22
import math
a, b, c = map(int, input().split())
gcd = math.gcd(math.gcd(a, b), c)
gcd = int(gcd)
temp1 = -1 + a // gcd
temp2 = -1 + b // gcd
temp3 = -1 + c // gcd
print(temp1 + temp2 + temp3)
