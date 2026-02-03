test=int(input())
q=[]
for i in range(test):
    n=int(input())
    a=list(map(int,input().split()))
    c={}
    for j in a:
        if j in c:
            c[j]+=1
        else:
            c[j]=1
    for k in c:
        if c[k]==1:
            b=a.index(k)
    print(b+1)


    