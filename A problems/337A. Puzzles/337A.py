a=int(input())
b=list(map(int,input().split()))
i=0
c=sorted(b)
e=c
d=[]
while i<a:
  if c[i]==c[a-1]:
     for j in range(a):
        e[a-1]+=1
        if e[a-1] not in b:
           x=e.index(e[a-1])
           b[x]=e[a-1]
           break
     r=[]
     
     r1=e.index(c[i])+1
     r2=e.index(c[a-1])+1
     r.append(r1)
     r.append(r2)
     d.append(r)
     i+=1
     a-=1         
    
  else:
    r=[]
    r1=b.index(c[i])+1
    r2=b.index(c[a-1])+1
    r.append(r1)
    r.append(r2)
    d.append(r)
    i+=1
    a-=1
for k in range(a):
    print(*d[k])



