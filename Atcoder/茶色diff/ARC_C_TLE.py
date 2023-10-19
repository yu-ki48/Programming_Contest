# https://atcoder.jp/contests/arc086/tasks/arc086_a

n, k = map(int, input().split())
A = list(map(int, input().split()))

kosuu = []
ans = 0

A_t = set(A)

nagasa = len(A_t)

if nagasa <= k:
    print(0)

else:    
    for t in A_t:
        kosuu.append(A.count(t))

    kosuu.sort()

    for t2 in range(nagasa - k):
        ans += kosuu[t2]

    print(ans)
