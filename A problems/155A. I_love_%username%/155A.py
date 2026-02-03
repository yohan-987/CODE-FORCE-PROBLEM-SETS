t=int(input())
n=list(map(int,input().split())) [:t]
c=0
best=n[0]
worst=n[0]
for i in range(len(n)-1):
    if best<n[i+1]:
        c+=1
        best=n[i+1]
    elif worst>n[i+1]:
        c+=1
        worst=n[i+1]
     
print(c)