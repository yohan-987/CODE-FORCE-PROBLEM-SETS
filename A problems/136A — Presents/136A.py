n=int(input())
a=input().split()
b=list(map(int,a))
d=[]
for i in range(1,n+1):
    if i in b:
        e=b.index(i)
        d.append(e+1)
print(*d)        
