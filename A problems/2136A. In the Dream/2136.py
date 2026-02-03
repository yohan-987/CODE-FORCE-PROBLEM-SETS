t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    b,c=max(a[0],a[1]),min(a[0],a[1])
    d,e=max(a[2]-a[0],a[3]-a[1]),min(a[2]-a[0],a[3]-a[1])
    if b<=2*c+2 and d<=2*e+2:
        print("YES")
    else:
        print("NO")



    