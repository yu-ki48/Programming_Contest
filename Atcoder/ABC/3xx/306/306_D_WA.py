# https://atcoder.jp/contests/abc306/tasks/abc306_d

n = int(input())
x = []
y = []
max_list = []
status = 0
hazi = 0
ans = 0
s = 0
for t in range(n):
    x_t, y_t = map(int, input().split())
    x.append(x_t)
    y.append(y_t)
ind = [j for j, t2 in enumerate(x) if t2 == 0]
for t2 in ind:
    max_list.append(max(ind[s:t2]))
    s = t2 
print(max_list)

if sum(x) == n:
    print(0)
if sum(x) == 0:
    ans = sum([ i for i in y if i >= 0])
    print(ans)
# else:
#     for t1 in ind:
#         if status == 0:
#             temp = ans
#             ans += max(max(y[hazi:t1]),0)
#             if temp != ans:
#                 status = 1
#         if status == 1:
#             if  

