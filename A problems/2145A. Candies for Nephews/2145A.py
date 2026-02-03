t=int(input())
c=[]
for i in range(t):
    a=int(input())
    if a%3==0:
        c.append(0)
    else:
        b= 3-(a%3)
        c.append(b)
for i in range(t):
    print(c[i])