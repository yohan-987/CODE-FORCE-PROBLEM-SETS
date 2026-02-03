n=int(input())
l=[]
for i in range(n):
     t=int(input())
     l.append(t)
     
for i in range(n):
     if l[i]<3:
          print("0") 
          continue
     if l[i]>=3:
          if l[i]%2==0:
            a=l[i]//2-1
            print(a)
          if l[i]%2!=0:
              a=l[i]//2
              print(a)