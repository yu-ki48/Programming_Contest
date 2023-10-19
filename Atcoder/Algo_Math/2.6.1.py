n, s = map(int, input().split())
A = list(map(int, input().split()))

answer = "No"
for i in range(0, 1 << n):
    partsum = 0
    for j in range(0, n):
        if (i & (1 << j)) != 0:
            partsum += A[j]
    if partsum == s:
        answer = "Yes"
        break

print(answer)