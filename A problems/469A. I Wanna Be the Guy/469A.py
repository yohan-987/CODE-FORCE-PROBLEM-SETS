n=int(input())
a=input().split()
b=input().split()
p=a[0]
q=b[0]
k=[]
for i in range(1,len(a)):
    if a[i] not in k:
        k.append(a[i])
for j in range(1,len(b)):
    if b[j] not in k:
        k.append(b[j])   
#print(k)        
if len(k)==n:
    print("I become the guy.")                   
else:
    print("Oh, my keyboard!")    