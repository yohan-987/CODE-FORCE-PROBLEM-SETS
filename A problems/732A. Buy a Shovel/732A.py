a=input().split()
cost=int(a[0])
change=int(a[1])
for i in range(1,10000000):
    if (cost*i)%10==0 or (cost*i)%10==change:
        print(i)
        break
    
    
   