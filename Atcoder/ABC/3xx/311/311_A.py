# https://atcoder.jp/contests/abc311/tasks/abc311_a

n = int(input())
s = input()
ch_a = 0
ch_b = 0
ch_c = 0
ch = 0
for t in s:
    ch += 1
    if t == 'A':
        ch_a += 1
    if t == 'B':
        ch_b += 1
    if t == 'C':
        ch_c += 1
    if ch_a != 0 and ch_b != 0 and ch_c != 0:
        print(ch)
        break