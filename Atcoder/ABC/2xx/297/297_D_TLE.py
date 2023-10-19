# https://atcoder.jp/contests/abc297/tasks/abc297_d

a, b = map(int, input().split())
counter = 0
while a != b:
    if a > b:
        a = a - b
        counter += 1
    else:
        b = b - a
        counter += 1
print(counter)