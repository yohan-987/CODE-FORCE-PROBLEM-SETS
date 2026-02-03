n=int(input())
count=0
for i in range(n):           # Read one line and split it into 3 separate values assigning each line values like 101 111 001 from values variable
    values= input().split()  # Read one line  and split it into 3 separate values so they have different index (like in array)
     #in split function it is necessary to enter values with space since its a string 
    total= int(values[0]) + int(values[1]) + int(values[2])  #we int here to change string to integer since in value we input which always store in string data type
    if total>=2:
       count +=1   #increment by 1                                                 
print(count)    