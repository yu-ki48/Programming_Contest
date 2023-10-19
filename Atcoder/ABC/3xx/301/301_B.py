# https://atcoder.jp/contests/abc301/tasks/abc301_b

n = int(input())
a = list(map(int, input().split()))
list1 = []
for t in range(n-1):
    list1.append([a[t],a[t+1]])

def sounyu(temp):
    if temp[1] > temp[0]:
        for t in range(temp[0]+1,temp[1]):
            temp.insert(-1,t)
    else:
        for t in range(temp[0]-1,temp[1],-1):
            temp.insert(-1,t)
    return temp[:-1]

for t in range(n-1):
    print(*sounyu(list1[t]), end=" ")
print(a[n-1])