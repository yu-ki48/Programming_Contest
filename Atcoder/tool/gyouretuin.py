import numpy as np
h, w = map(int, input().split())
A = [list(map(int, input().split())) for i in range(h)]
A = np.array(A)
print(A)
print(A[:, 0])
print()
print(A)
B = [[0 for k in range(w)] for l in range(h)]
print(B)