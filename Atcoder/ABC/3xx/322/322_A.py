# https://atcoder.jp/contests/abc322/tasks/abc322_a

n = int(input())
s = input()

ind = s.find('ABC')

if ind != -1:
    print(ind+1)
else:
    print(ind)