# https://atcoder.jp/contests/abc295/tasks/abc295_b

r, c = map(int, input().split())

B = [list(input()) for _ in range(r)]

def hyouzi(r,c,B):
    for i_1 in range(r):
        for j_1 in range(c):
            print(B[i_1][j_1], end='')
        print()



def manhattan(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

kabe = []

bakudan = []

bakudan_size = []

for i in range(r):
    for j in range(c):
        if B[i][j] == '#':
            kabe.append((i,j))
        elif B[i][j] != '.':
            bakudan.append((i,j))
            bakudan_size.append(B[i][j])
            B[i][j] = '.'

if len(bakudan) == 0:
    hyouzi(r,c,B)
else:
    for k in kabe:
        ind = 0
        for l in bakudan:
            if manhattan(k,l) <= int(bakudan_size[ind]):
                B[k[0]][k[1]] = '.'
            ind += 1
    hyouzi(r,c,B)


 