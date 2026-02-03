n=[]
for i in range(5):
    r=list(map(int,input().split()))
    n.append(r)
#print(n[2][1])
a=0
b=0
for i in range(5):
    if 1 in n[i]:
        a=i+1
        b=n[i].index(1)+1
        break
#print(a,b)
if a<=3 and b<=3: 
  s=(3-a)+(3-b)
elif a>3 and b<=3:
    s=(a-3)+(3-b)
elif a>3 and b>3:
    s=(a-3)+(b-3)
elif a<=3 and b>3:
    s=(3-a)+(b-3)
print(s)