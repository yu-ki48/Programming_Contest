# https://atcoder.jp/contests/abc296/tasks/abc296_c

def hantei(A):
    for t1 in A:
        if t1 + x in A:
            return 1
        
n, x = map(int, input().split())
A = set(map(int, input().split()))
B = list(A)
if hantei(A) == None:
    print('No')
else:
    print('Yes')

