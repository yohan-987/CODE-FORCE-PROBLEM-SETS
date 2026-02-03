t=int(input())
c=[]
for i in range(t):
    n=int(input())
    s=input()
    d=sorted(s)
    d=''.join(d)

    if d=="Timru":   #Uppercase comes before lowercase in ASCII code
        c.append("YES")
    else:
        c.append("NO")
for i in range(t):
    print(c[i])
