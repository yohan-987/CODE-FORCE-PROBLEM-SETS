n=int(input())
b=input().upper()[:n]
a=0
d=0
for i in b:
    if i=="A":
        a+=1
    if i=="D":
        d+=1
if a>d:
    print("Anton")        
if d>a:
    print("Danik")
if a==d:
    print("Friendship")