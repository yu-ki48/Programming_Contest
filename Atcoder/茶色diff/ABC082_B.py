# https://atcoder.jp/contests/abc082/tasks/abc082_b

s = input()
t = input()

s_sorted = sorted(s)
t_sorted = sorted(t, reverse=True)

s_sorted = ''.join(s_sorted)
t_sorted = ''.join(t_sorted)

if s_sorted < t_sorted:
    print('Yes')
else:
    print('No')