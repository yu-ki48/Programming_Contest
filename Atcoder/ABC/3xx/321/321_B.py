# https://atcoder.jp/contests/abc321/tasks/abc321_b

n, x = map(int, input().split())

A = list(map(int, input().split()))

A_max = max(A)
A_min = min(A)

A_sum = sum(A)

A_sum_t = A_sum - (A_max + A_min)

if A_sum_t >= x:
    print(0)
elif A_sum_t < x:
    if (x - A_sum_t) <= A_min:
        print(0)
    elif (x - A_sum_t) <= A_max:
        print(x - A_sum_t)
    else:
        print(-1)  


