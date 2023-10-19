# https://atcoder.jp/contests/abc313/tasks/abc313_a

n = int(input())
p = list(map(int, input().split()))
if n > 1:
    p_1 = p[0]
    p_m = max(p[1:])

    if p_1 > p_m:
        print(0)
    else:
        print(p_m - p_1 + 1)
else:
    print(0)
