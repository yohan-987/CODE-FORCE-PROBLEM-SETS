n = input()
i = 0
valid = True
while i < len(n):
    if n.startswith("144", i):
        i += 3
    elif n.startswith("14", i):
        i += 2
    elif n.startswith("1", i):
        i += 1
    else:
        valid = False
        break
if valid:
    print("YES")
else:
    print("NO")
