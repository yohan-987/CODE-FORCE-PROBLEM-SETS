k=int(input())
a=input().split()
count=0
b=0
m=sorted(a,reverse=True)
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
