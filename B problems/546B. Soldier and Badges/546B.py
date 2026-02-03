n=int(input())
s=input().split()
e=list(map(int,s))
b=sorted(e)
c=0
for j in range(n):
    if b[j] in b:
      for i in range(n-1):  
       if b[i]==b[i+1]:
          b[i+1]=b[i+1]+1
          c+=1
          break
print(c)
    