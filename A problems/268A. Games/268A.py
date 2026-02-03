n=int(input()) #number of teams 
counter=0
h=[]
a=[]
for k in range(n):
    c=input().split()
    h1=int(c[0])   #home 
    a1=int(c[1])   #guest
    h.append(h1)
    a.append(a1)
for i in range(n):
    for j in range(n):
        if h[i]==a[j]:
            counter+=1
print(counter)            