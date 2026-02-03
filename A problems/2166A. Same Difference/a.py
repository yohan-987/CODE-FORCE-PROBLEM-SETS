t=int(input())
for i in range(t):
    n=int(input())
    a=input()
    m = max(set(a), key=a.count)
    c=0
    for i in range(n):
        if m!=a[i]:
            c+=1
    print(c)

        
    