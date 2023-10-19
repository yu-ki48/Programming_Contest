# https://atcoder.jp/contests/abc309/tasks/abc309_a

a, b = map(int, input().split())
if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 4 and b == 5) or (a == 5 and b == 6) or (a == 7 and b == 8) or (a == 8 and b == 9):
    print('Yes')
else:
    print('No')