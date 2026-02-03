n=input().split()
a=list(n)
counter=0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
       counter+=1
       
    else:
      j=i
      while j<=len(a)-2:
        if a[i]==a[j+1]:
          counter+=1
          j+=1
        else:
           j+=1
           counter+=0 
print(counter)       

