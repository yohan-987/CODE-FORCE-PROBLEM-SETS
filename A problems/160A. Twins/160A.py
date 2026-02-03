n=int(input())
a=input().split()
s=sorted(list(map(int,a)))
s.reverse()  #we need to take biggest coins first 
#s1=s[0]
s1=0
s2=0
count=0
for i in range(n):
    s2+=s[i]
for i in range(n):
        count+=1
        s1+=s[i]
        s2-=s[i]
        if s1>s2 :
           break
print(count)        
    