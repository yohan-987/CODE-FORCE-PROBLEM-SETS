t=int(input())
a=list(map(int,input().split()))
i=0
r=0
s=0
d=0
l=len(a)-1

while r<l+1:
    if i%2==0:
        if a[r]>a[l]:
            s+=a[r]
            r+=1
        else:
            s+=a[l]
            l-=1
    else:
        if a[r]>a[l]:
            d+=a[r]
            r+=1
        else:
            d+=a[l]
            l-=1
    i+=1
print(s,d)
