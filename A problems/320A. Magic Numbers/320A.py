n=input()
a=0

i=0
while i<len(n):
    if n.startswith("144",i):
        a+=3
        i+=3
    elif n.startswith("14",i):
        a+=2
        i+=2
    elif n.startswith("1",i):
        a+=1
        i+=1
    else:
        break
if a==len(n):
    print("YES")
else:
    print("NO")
