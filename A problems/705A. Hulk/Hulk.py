n=int(input())
c=[]
for i in range(n):
        if i==0:
                c.append('I hate')

        if i>0 and i%2==0:
                c.append(' I hate')

        elif i>0 and i%2!=0:
                c.append(' I love')
m=' that'.join(c)+' it'   
print(m)            