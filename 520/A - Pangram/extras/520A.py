n=int(input())
a=input().lower()[:n]
u=""    #string of unique letters , used to check inside loop to make sure letter doesn't repeat
counter=0

for j in a:
        if 'a'<=j<='z' and j not in u:
            u+=j
            counter+=1
if counter==26:
    print("YES")    
else:
    print("NO")      