# https://atcoder.jp/contests/abc310/tasks/abc310_c

n = int(input())
ans = set()
temp = input()
ans.add(temp)
for t in range(n-1):
    temp1 = input()
    temp2 = temp1[::-1]
    if temp1 not in ans and temp2 not in ans:
        ans.add(temp1)
 
print(len(ans))