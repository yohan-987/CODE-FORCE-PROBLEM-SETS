n=input().split()
a=int(n[0])
b=int(n[1])
m=a
for i in range(b):
    if m%10==0:
        m= m//10
    else:
        m=m-1
print(m)        