# https://atcoder.jp/contests/abc305/tasks/abc305_b

p, q = map(str, input().split())
mydict = {"A":0, "B":3, "C":4, "D":8, "E":9, "F":14, "G":23}

print(abs(mydict[p] - mydict[q]))