# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_j

n = int(input())
def kaijou(n):
    if n == 1:
        return 1
    return n * kaijou(n-1)

print(kaijou(n))