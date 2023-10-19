# https://atcoder.jp/contests/abc299/tasks/abc299_c

def hantei(x, n):  
    ch = 0
    temp = []
    for i in range(n):
        if x[i] == 'o':
            ch += 1
        elif x[i] == '-':
            temp.append(ch)
            ch = 0
    temp.append(ch)
    print(max(temp))
 
n = int(input())
s = input()
if 'o' not in s or '-' not in s:
    print(-1)
else:
    hantei(s, n)