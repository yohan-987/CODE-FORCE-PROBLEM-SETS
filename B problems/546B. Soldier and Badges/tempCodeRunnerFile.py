n=int(input())
s=input().split()
count=0

d=""
for i in range(n):
  c=0
  for k in range(n-1):
    if s[k]==s[k+1]:
       c+=1
    
    for j in s:
        if j not in d and c>0:
            d+=j
        elif j in d and c>0:
            d+=j
            count+=1
print(count)        
    