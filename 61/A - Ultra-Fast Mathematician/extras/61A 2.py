a=input()
n=len(str(a))
b=input()[:n]
e=''
j='0'
k='1'
for i in range(n):
    if a[i]==b[i]:
        e+=j
    else:
        e+=k   
print(e)
 