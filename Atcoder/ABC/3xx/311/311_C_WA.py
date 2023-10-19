# https://atcoder.jp/contests/abc311/tasks/abc311_c

n = int(input())
A = list(map(int, input().split()))
ch = 0
grah = []
for t in range(1, n+1):
    grah.append((t,A[t-1]))
goal = -1
for t2 in range(1, n+1):
    start = grah[t2-1][0]
    ans = []
    for t3 in range(1, n+1):
        next = grah[t2-1][1]
        goal = grah[next-1][1]
        t2 = goal
        ans.append(goal)
        if start == goal and ch == 0:
            if len(ans) == 1:
                if ans[0] == grah[ans[0]][1]:
                    ans.append(grah[ans[0]][0])
                else:
                    ans.append(grah[ans[0]][1])
            print(len(ans))
            ch = 1
        if ch == 1:
            break
ans.reverse()
print(*ans)        
            