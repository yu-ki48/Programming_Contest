# https://atcoder.jp/contests/abc308/tasks/abc308_c

n = int(input())
ansd = {}
ruiseki = -0.000000001
for t in range(1,n+1):
    a, b = map(int, input().split())
    a = a / (a+b)
    ansd[a] = t
    
print(ansd)
ansd = sorted(ansd.items(), reverse=True)
for temp in ansd.values():
    print(temp, end=' ')

