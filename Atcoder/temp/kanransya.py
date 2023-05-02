n, m = map(int, input().split())
a = []
b = []
c = [0] * n
for t in range(n):
    a.append(int(input()))
for t in range(m):
    b.append(int(input()))
ch1 = 0
ch2 = 0
print(a)
print(b)
size = len(a)
for t in b:
    while b[ch2] > 0:
        if b[ch2] > a[ch1]:
            c[ch1] += a[ch1]
            b[ch2] -= a[ch1]
            ch1 = (ch1 + 1) % size
        else:
            c[ch1] += b[ch2]
            b[ch2] = 0
            ch1 = (ch1 + 1) % size
    ch2 += 1
for t in c:
    print(t)

