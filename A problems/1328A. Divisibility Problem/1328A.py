t=int(input())
for i in range(t):
    a=input().split()
    x=int(a[0])
    y=int(a[1])
    counter=0
    for j in range(1000000000): #Brute force , doesn't work , takes so much time 
     if x%y!=0:
        counter+=1
        x+=1
     else:
        print(counter) 
        break   
       