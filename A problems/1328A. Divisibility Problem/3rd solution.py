t=int(input())
for i in range(t):
    a=input().split()
    x=int(a[0])
    y=int(a[1])
    counter=0
    for j in range(y): #why range y? = because the number need to add to the x to make it divisible will always be smaller than y , its actually n=y-(x%y)
     if x%y!=0:
        counter+=1
        x+=1
     else:
        print(counter) 
        break   
       