n=int(input())
a=input().lower()
c=[]
counter=0
for i in range(n):
    if 'a'<=a[i]<='z' and a[i] not in c:
            counter+=1
            c.append(a[i])
if counter==26:
      print("YES")
else:
      print("NO")      
