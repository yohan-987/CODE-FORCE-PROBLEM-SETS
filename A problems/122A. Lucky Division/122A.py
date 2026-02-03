n=input()     #in loop int is not iterable 
counter=0
b=int(n)
k=0
p=0
for i in n:
        if i=='7' or i=='4':   #i is string and should be compared with string
            counter+=1
if counter==len(n):   
        a=int(n)
        check_a=True
else:
        check_a=False
e=[4,7,44,47,74,77,444,447,477,474,744,747,774,777]        
if b%4==0 or b%7==0 or (check_a and b % a == 0):
       print("YES")
       k+=1
if k==0:
       for i in e:
              if b%i==0:
               print("YES")
               p+=1
               break
              
if p==0 and k==0:
       print("NO")

#(check_a and b % a == 0) ensures that Python only evaluates b % a if check_a is True.

# If check_a is False, Python does not try b % a, so no error occurs.