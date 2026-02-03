'''
n=10 , k=5
 1 2 3 4 ......10 (first 10 natural numbers)
 1 3 5 7 9 2 4 6 8 (first write all odd and then all even)
 kth postion = [k-1] = 9
'''
a=input().split()
n=int(a[0])
k=int(a[1])
c=[]
if n%2==0:
        p=n//2
        for j in range(p):
            d=2*j+1
            c.append(d)
        for j in range(p):
            d=2*j+2
            c.append(d)  
if n%2!=0:
    p=n//2+1
    for j in range(p):
            d=2*j+1
            c.append(d)
    for j in range(p-1):
            d=2*j+2
            c.append(d)  
print(c[k-1])
