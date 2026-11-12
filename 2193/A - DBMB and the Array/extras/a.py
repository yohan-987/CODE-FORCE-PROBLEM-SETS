t=int(input())
for i in range(t):
    n,s,x=map(int,input().split())
    a=list(map(int,input().split()))

    current=sum(a)
    
    if s>=current and (s-current)%x==0:
                print("YES")
    else:
                print("NO")