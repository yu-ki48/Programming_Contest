# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_n

num = int(input())
def soinsubunkai(n):
    ans = []
    LIMIT = int(n ** 0.5)
    for i in range(2, LIMIT + 1):
        while n % i == 0:
            n /= i
            ans.append(i)
    if n >= 2:
        ans.append(int(n))
    return ans
print(*soinsubunkai(num))

