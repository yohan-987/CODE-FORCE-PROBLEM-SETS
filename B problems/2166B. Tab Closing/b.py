t=int(input())
for i in range(t):
    a,b,n=map(int,input().split())
    m=n
    
    l=min(b,a/m)
    if l<b :
        print(2)
    else:
        print(1)
