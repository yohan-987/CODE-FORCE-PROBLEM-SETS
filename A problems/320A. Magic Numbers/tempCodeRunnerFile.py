n=input()
a=0
b=0
c=0
i=0
while i<len(n):
    if n.startswith("144",i):
        a+=3
        i+=3
    elif n.startswith("14",i):
        b+=2
        i+=2
    elif n.startswith("1",i):
        c+=1
        i+=1
if a+b+c==len(n):
    print("YES")
else:
    print("NO")
