a=input()
n=len(str(a))
b=input()[:n]
e=''
for i in range(n):
    if a[i]==b[i]:
        e+='0'
    else:
        e+='1'  
print(e)
 