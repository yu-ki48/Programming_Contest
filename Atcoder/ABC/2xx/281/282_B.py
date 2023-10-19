# https://atcoder.jp/contests/abc281/tasks/abc281_b

s = input()
 
if len(s) != 8 or s[0].isdigit() or s[7].isdigit():
  print("No")
elif not s[1:7].isdecimal() or s[1] == '0':
  print("No")
else:
  print("Yes")