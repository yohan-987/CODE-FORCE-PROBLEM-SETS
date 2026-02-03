#this is correct but there are too much uneeded calculations and is not time efficient for big values


n=int(input())
l=[]
for i in range(n):
     t=int(input())
     l.append(t)
     
for i in range(n):
     if l[i]<3:
          print("0") 
     if l[i]>=3:
          a=l[i]
          b=0
          if l[i]%2==0:
           p=l[i]//2
          if l[i]%2!=0:
            p=l[i]//2+1 
          
          for j in range(len(l)):
               counter=0
               j=1
               while j<p:   
                   if (a-j)+(b+j)==l[i]:
                    counter+=1
                    j+=1
          print(counter)            
                   
       