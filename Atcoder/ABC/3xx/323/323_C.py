# https://atcoder.jp/contests/abc323/tasks/abc323_c

n, m = map(int, input().split())

A = list(map(int, input().split()))
A_i = []
for temp in range(len(A)):
    A_i.append((A[temp],temp))
A_s = sorted(A_i, key=lambda x:x[0], reverse=True)

score_list = []
nokori = []
for i in range(n):
    s = input()
    score = i + 1
    nokori_i = []
    for j in range(m):
        if s[A_s[j][1]] == 'o':
            score += A_s[j][0]
        else:
          nokori_i.append(A_s[j][0])
    score_list.append(score)
    nokori.append(nokori_i)
max_score = max(score_list)

for k in range(n):
    l = 0
    while score_list[k] < max_score:
        score_list[k] += nokori[k][l]
        l += 1
    print(l)
