n=int(input())
c=input()[:n]
d=list(c)
count=0
for i in range(len(d)-1):
     if d[i]==d[i+1]:
        count+=1
print(count)
