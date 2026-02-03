n=int(input())

a=input().upper()
b=''.join(sorted(a))

counter=0    
for j in range(len(b)-1):  
      
       if b[0]<=b[j]:    
           counter+=1
if counter>3:
      print("Anton")
if counter==3:
       print("Friendship")    
if counter<3:
      print("Danik")               
      


'''  why len(b)-1??
       🔍 Example:

Say b = "ABC"
→ length = 3
→ valid indexes = 0, 1, 2

range(len(b))     → range(3)  →  [0, 1, 2]
range(len(b)-1)   → range(2)  →  [0, 1]
✅ When j = 0, we compare b[0] with b[1]
✅ When j = 1, we compare b[1] with b[2]
🚫 If we allowed j = 2, then b[2+1] → b[3] doesn’t exist → crash.
       
       
       '''
