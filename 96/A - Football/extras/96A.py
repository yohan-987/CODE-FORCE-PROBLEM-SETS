n=input()
a=list(n)
found=0
count=1 #to count first player too 
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        count+=1
    if count==7:
        found=1
        break
    elif a[i]!=a[i+1]:
        count=1
if found==1:
    print("YES") 
else:
    print("NO")           
