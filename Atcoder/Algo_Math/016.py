# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_p

n = int(input())
a = list(map(int, input().split()))
def euclid(n1, n2):
    while n1 >= 1 and n2 >= 1:
        if n1 > n2:
            n1 = n1 % n2
        else:
            n2 = n2 % n1
    if n1 >= 1:
        return n1
    else:
        return n2

ans = euclid(a[0],a[1])
for i in range(2,n):
    ans = euclid(ans, a[i])
print(ans)

