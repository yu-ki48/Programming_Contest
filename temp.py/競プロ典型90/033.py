#コーナーケース(縦か横が1のときに気をつける)
h, w = map(int, input().split())
 
def hantei(t):
    if t % 2 == 0:
        return t // 2
    else:
        return (t + 1) // 2
    
if h == 1 or w == 1:
    print(h * w)
else:
    print(hantei(h) * hantei(w))