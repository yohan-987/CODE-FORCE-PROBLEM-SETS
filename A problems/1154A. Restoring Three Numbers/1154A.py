n=input().split()
d=sorted(list(map(int,n)))
abc=d[3] #a+b+c
ab=d[0]  #a+b
bc=d[1]  #b+c
ca=d[2]  #c+a

a1=d[2] #a+c
a2=d[0]-d[1] #a-c

a=(a2+a1)//2

b=d[0]-a

c=d[1]-b

print(a,b,c,end=" ")



