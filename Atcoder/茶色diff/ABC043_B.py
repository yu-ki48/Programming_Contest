# https://atcoder.jp/contests/abc043/tasks/abc043_b

s = list(input())
q = []
for t in s:
    if t != 'B':
        q.append(t)
    elif len(q) == 0:
        continue
    else:
        q.pop(-1)
for t2 in q:
    print(t2, end='')
