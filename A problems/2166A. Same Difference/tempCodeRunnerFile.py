t=int(input())
for i in range(t):
    n=int(input())
    a=input()
    d=max(a)
    c=0
    for i in range(n):
        if d!=a[i]:
            c+=1
    print(c)

        
    