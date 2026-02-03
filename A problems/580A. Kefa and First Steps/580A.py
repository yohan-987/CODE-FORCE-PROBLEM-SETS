n=int(input())
a=list(map(int,input().split()))
c=[]
e=[1]
d=1
for i in range(n-1):
    if a[i]<=a[i+1]:   
        d+=1
        e[0]=d     #for cases like 10 ,1 2 3 4 1 2 3 4 5 6 = where condition is met till last digit so else won't append it
    else:
        c.append(d)
        d=1
if d==n:
    print(d)   
else:
  c.append(e[0])     
  c.sort()
  print(c[-1])