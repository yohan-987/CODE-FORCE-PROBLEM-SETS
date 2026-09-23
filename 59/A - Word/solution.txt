a=input()
u=0
l=0
b=a.upper() 
c=a.lower()
for i in a:
    if "a"<=i<="z":
        l+=1
    elif "A"<=i<="Z":
        u+=1
if u>l:
     print(b)
else:
    print(c)     