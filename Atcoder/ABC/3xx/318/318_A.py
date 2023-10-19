# https://atcoder.jp/contests/abc318/tasks/abc318_a

n, m, p = map(int, input().split())

di = n - m

print((di // p) + 1)