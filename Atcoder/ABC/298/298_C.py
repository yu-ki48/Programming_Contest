# https://atcoder.jp/contests/abc298/tasks/abc298_c

n = int(input())
q = int(input())
def sousa1(i,j,hako, num):
    hako[j-1].append(i)
    num[i-1].add(j)
    
def sousa2(i,hako):
	hako[i-1].sort()
	print(*hako[i-1])
    
def sousa3(i,num):
    num[i-1] = list(num[i-1])
    num[i-1].sort()
    print(*num[i-1])
    num[i-1] = set(num[i-1])
    
hako = [[] for i in range(n)]
num = [set() for i in range(2 * 10 ** 5)]
for t in range(q):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        sousa1(temp[1],temp[2],hako, num)
    elif temp[0] == 2:
        sousa2(temp[1], hako)
    else:
        sousa3(temp[1], num)