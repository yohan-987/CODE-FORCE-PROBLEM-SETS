a=input().split()
n=int(a[0])
t=int(a[1])
x=input()
c=list(x)

for t in range(t):
  i=0
  while i<n-1:
    if c[i] == 'B' and c[i+1] == 'G':
        c[i],c[i+1]=c[i+1],c[i]
        i+=2
    else:
       i+=1     
print("".join(c))
