n=int(input())
c=list(map(int,input().split()))
l=len(c)-1
r=0
s=[]
d=[]
T=0
while l>=r:
    if c[r]>c[l]:
        
        if T%2==0:
          s.append(c[r]) 
        else:
          d.append(c[r])
        r+=1 
        T+=1      
    else:
        
        if T%2==0:
          s.append(c[l]) 
        else:
          d.append(c[l]) 
        l-=1
        T+=1       
    
print(sum(s),sum(d))
