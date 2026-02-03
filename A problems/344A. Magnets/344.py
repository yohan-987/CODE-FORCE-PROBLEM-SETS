n=int(input())
a=[]
for i in range(n):
    b=int(input())
    a.append(b)
count=1
for j in range(len(a)-1):
    if a[j]!=a[j+1]:
        count+=1
print(count)        