a=input()
u=0
l=0
#b=a.upper() 
#c=a.lower()
for i in a:
   # if "a"<=i<="z":  (we can skip this and can write as)
    if i.islower():     #this way only lowercase of anything will count
        l+=1
    else:
        u+=1
if u>l:
     print(a.upper())    #we can also write it like this
else:
    print(a.lower())     