k=int(input())
a=input().split()
y=[]
for i in range(len(a)):
    e=int(a[i])
    y.append(e)
z=0    
for i in range(len(a)):
    z=z+y[i]
if k>z:
    print("-1")
else:   
    count=0
    b=0   
    m=sorted(y,reverse=True)
    for i in range(len(a)):
     if b+int(m[i])<k:
        count+=1
        b=b+int(m[i])
     elif b+int(m[i])>=k:
        count+=1
        break
    if k==0:    
     print(0)
   
    else:
     print(count)
