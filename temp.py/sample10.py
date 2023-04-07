import numpy as np
n = int(input())
a = input()
a = a.split(' ')
a = [int(s) for s in a]
b = sorted(a)
temp1 = b[n:-n]
temp2 = np.mean(temp1)
print(temp2)
