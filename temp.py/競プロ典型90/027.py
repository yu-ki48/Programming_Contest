n = int(input())
name = set()
for t in range(1, n + 1):
    name_temp = input()
    if name_temp not in name:
        name.add(name_temp)
        print(t)
    

