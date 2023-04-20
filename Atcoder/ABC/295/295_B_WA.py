# 未完成
# https://atcoder.jp/contests/abc295/tasks/abc295_b
r, c = map(int, input().split())
B = []
for i in range(r):
  B.append(input())
print(B)
for t1 in range(r):
    for t2 in range(c):
        if B[t1][t2].isdecimal():
            for t3 in range(r):
                for t4 in range(c):
                    if abs(t1-t3) + abs(t2-t4) <= int(B[t1][t2]):
                        B[t1][t2] = '.'


 