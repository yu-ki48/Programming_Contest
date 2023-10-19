# https://atcoder.jp/contests/abc292/tasks/abc292_c

n = int(input())
goukei = 0
def counter(num):
    count = 0
    for t in range(1, num + 1):
        if num % t == 0:
            count += 1
    return count

for temp in range(1, n):
    temp1 = 0
    temp2 = 0
    temp1 += counter(temp)
    temp2 += counter(n - temp)
    goukei  += temp1 * temp2
print(goukei)