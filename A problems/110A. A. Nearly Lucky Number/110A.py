n=input()     #in loop int is not iterable 
counter=0
for i in n:
        if i=='7' or i=='4':   #i is string and should be compared with string
            counter+=1
if counter==4 or counter==7:   #because nearly lucky case , becuase '4' and '7' needs to appear 4 or 7 times despite being in mixed numbers
        print("YES")
else:
        print("NO")          
