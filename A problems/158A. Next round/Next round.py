a=input().split()#it will take numeber of partipants and the kth  participant as seperate strings
n=int(a[0])      #no. of participants
k=int(a[1])      #the position of particaipant which threshold for passing

b=input().split()  #it will take scores of the participants as a seperate strings
c=[]  #an empty array to fill the scores in 
for i in range(n):  #run till all the n participants scores are entered
    c.append(int(b[i]))
threshold=c[k-1]    #Everyone before K passed and kth position is actually at k-1 since index starts from zero
counter=0           #to count number of participants passed 
for j in range(n):
    if c[j] >= threshold and c[j] > 0:  #score should be greater than threshold and should be positive 
     counter+=1
print(counter)     

