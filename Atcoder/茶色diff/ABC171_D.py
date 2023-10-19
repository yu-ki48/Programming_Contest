# https://atcoder.jp/contests/abc171/tasks/abc171_d

n = int(input())

A = list(map(int, input().split()))
ans = [0] * (10 ** 5)

sum_a = sum(A)

for t1 in A:
  ans[t1-1] += 1
  
q = int(input())

for t in range(q):
    b, c = map(int, input().split())
    sum_a += (c - b) * ans[b-1]
    print(sum_a)
    ans[c-1] += ans[b-1]
    ans[b-1] = 0
