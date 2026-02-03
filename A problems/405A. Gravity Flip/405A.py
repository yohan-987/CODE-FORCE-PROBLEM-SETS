n=int(input())
a=input().split()  #its string and we can't compare strings like integers because for eg '10'<'2' as a string so it would provide wrong output 
c=[]
for k in range(n):
   c.append(int(a[k])) 
for j in range(n):
 for i in range(0,n-j-1):
    if c[i]>c[i+1]:
        c[i],c[i+1]=c[i+1],c[i]
print(*c)       #gives spaced integers , not using " ".join(c) because it is used to compare integers 











'''

Input
6
100 40 60 20 1 80
Output
1 100 20 40 60 80
Answer
1 20 40 60 80 100 
Checker Log
wrong answer 2nd numbers differ - expected: '20', found: '100'

'''