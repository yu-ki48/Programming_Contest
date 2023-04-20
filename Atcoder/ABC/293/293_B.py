# https://atcoder.jp/contests/abc293/tasks/abc293_b

n = int(input())
A = input()
A = A.split(' ')
A = list(map(int, A))
ind = [0]*n
ch = 0
for t1 in A:
  if ind[ch] == 0:
    ind[t1-1] += 1
  ch += 1
print(ind.count(0))
for t2 in range(n):
  if ind[t2] == 0:
    print(t2 + 1, end='')
    print(' ', end='')