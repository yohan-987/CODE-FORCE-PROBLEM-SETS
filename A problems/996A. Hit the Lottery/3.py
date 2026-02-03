n=int(input())
c=[100,20,10,5,1]
count=0
for i in range(len(c)):
     if n>=c[i]:
        count+=n//c[i]
        n=n%c[i]
print(count)         

