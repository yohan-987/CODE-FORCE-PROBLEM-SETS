n=input().split()
a=int(n[0])
k=int(n[1])
c=0
d=[]
j=1
if a%2==0:
    c=a//2
else:
    c=a//2+1    
if k<=c:
   f=1+(k-1)*2
else:
    f=2+(k-c-1)*2    #because even numbers are starting after c , odd numbers 
print(f)                