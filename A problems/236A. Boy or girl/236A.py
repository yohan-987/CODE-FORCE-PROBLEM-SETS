a=input().lower()
b=""   #an empty variable to fill it unique words , eg= Banana  = Ban
for i in a:  #runs a loop across the index of string a 
    if i not in b: #condition so that any string repeats then it would be jump out of if 
        b+=i
if len(b)%2==0:  #len because b is a string not an integer 
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")            

