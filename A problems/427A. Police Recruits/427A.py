n=int(input())
a=input().split()
counter=0
if int(a[0])==-1:
    counter+=1
else:
    counter=0    
i=1
while i<n:
   
    if int(a[i])==-1 and int(a[i-1])<0:
        counter+=1
        i+=1
    elif int(a[i])==1: 
        
        i+=1
    elif i+1<n and int(a[i])==1 and int(a[i+1])==1:
        i=i+2
    elif i<n and int(a[i])>1:
        i+=int(int(a[i]))
        
print(counter)