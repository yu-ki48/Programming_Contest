# https://atcoder.jp/contests/abc324/tasks/abc324_b

n = int(input())

def hantei(n):
    for i in range(61):
        for j in range(40):
            ans = (2 ** i) * (3 ** j)
            if ans == n:
                return True
    return False        
    
            
if hantei(n) == True:
    print('Yes')
else:
    print('No')