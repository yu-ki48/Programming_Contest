# https://atcoder.jp/contests/abc291/tasks/abc291_a

s = input()
i = 1
for temp in s:
    if temp.isupper() == True:
        print(i)
    i += 1
