t=int(input())
c=[]
for i in range(t):
    n=int(input())
    a=input()
    b=input()
    count=0
    c1=0
    c2=0
    for k in range(n):
        if a[k]=="R" and b[k]=="R":
            count+=1
    for j in range(n):
        if a[j]=="R":
            c1+=1
        if b[j]=="R":
            c2+=1
    z=max(c1,c2)
    if z==count:
        c.append("YES")
    else:
        c.append("NO")              
        
for i in range(t):
    print(c[i])
        