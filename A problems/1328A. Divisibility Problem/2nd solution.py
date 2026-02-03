t=int(input())
for i in range(t):
    a=input().split()
    x=int(a[0])
    y=int(a[1])
    if x%y==0:
        print("0")
    else:
        m=y-(x%y)   #an integer to add to make it divisible 
        print(m)