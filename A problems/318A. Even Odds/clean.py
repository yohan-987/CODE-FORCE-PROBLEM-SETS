a=input().split()
n=int(a[0])
k=int(a[1])
if n%2==0:
   p=n//2
else:
   p=n//2+1

if k<=p:
   print(2*k-1)   #AP
else: 
   print(2*(k-p))    #AP