n=int(input())   #Number of lines so we can enter multiple inputs at once
X=0  #the initial value
for i in range(n):  #gonna run a loop to cover each line 
     a=input()     #gonna take input for each line
     if "++" in a: #conditions for each line 
          X+=1      #operation on initial value
     else:
          X-=1
print(X)          