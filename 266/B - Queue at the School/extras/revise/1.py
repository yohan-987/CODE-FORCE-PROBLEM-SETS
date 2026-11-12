a=input().split()
n=int(a[0])
t=int(a[1])
l=input()
q=list(l)
j=0
for i in range(t):
       #for j in range(n-1):
       while j<n-1:
           if q[j]=='B' and q[j+1]=='G':
                 q[j],q[j+1]=q[j+1],q[j]
                 j+=2
           else:
                 j+=1
s=''.join(q)                 
print(s)                 