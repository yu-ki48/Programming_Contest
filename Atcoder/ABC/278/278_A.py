# https://atcoder.jp/contests/abc278/tasks/abc278_a

N = input()
K = N.split(' ')
A = input()
i = 0
ls = []
ls = A.split(' ')
K = int(K[1])
while i < int(K):
  ls.append('0')
  i += 1
temp1 = ls[K:]
temp2 = ' '.join(temp1)
print(temp2)