# https://ppg.paiza.jp/code_review_bingo/python/6/answers/new

a_list = list(map(str, input().split()))
b_list = list(map(str, input().split()))
a = ''.join(a_list)
b = ''.join(b_list)
if b == a:
    print("Yes")
else:
    print("No")