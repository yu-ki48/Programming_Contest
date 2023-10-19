# https://atcoder.jp/contests/abc324/tasks/abc324_c

temp = list(input())
n = int(temp[0])
t_a = temp[2:]
t_r = list(reversed(t_a))
a = []
b = []
s_list = []
ans = []


def calc(s, t):
     for i in range(len(t)):
        if i >= len(s):
            return len(s)
        if s[i] != t[i]:
            return i
     
     return len(t)

for j in range(n):
    s_list.append(list(input()))

for k in range(n):
    a.append(calc(s_list[k], t_a))

for l in range(n):
    s_list[l] = list(reversed(s_list[l]))
    b.append(calc(s_list[l], t_r))

for q in range(n):
    flag = False
    if a[q] == len(t_a) and len(s_list[q]) == len(t_a):
        flag = True
    if (a[q] + b[q]) >= len(t_a) and (len(t_a) + 1 == len(s_list[q])):
        flag = True
    if (a[q] + b[q]) >= (len(t_a) - 1) and (len(t_a) - 1 == len(s_list[q])):
        flag = True
    if (a[q] + b[q]) == (len(t_a) - 1) and len(t_a) == len(s_list[q]):
        flag = True
    if flag:
        ans.append(q+1)
    
print(len(ans))
print(*ans)  

    