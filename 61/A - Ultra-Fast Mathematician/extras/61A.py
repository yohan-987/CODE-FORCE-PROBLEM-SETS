a=int(input())
b=int(input())
n=len(str(a))
c=list(str(a))
d=list(str(b))[:n]
e=[]
for i in range(n):
    if c[i]==d[i]:
        e.insert(i,0)
    else:
        e.insert(i,1)   
print(e)

#this code is not working properly because in python if '0' comes first in string it will not count it 
#for eg -- 0123 would in str mean as 123 