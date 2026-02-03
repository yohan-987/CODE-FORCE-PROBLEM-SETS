a=input().split()
k=int(a[0])  #cost of first banana
n=int(a[1])  #money
w=int(a[2])  #number of banana

total=((w*(w+1))//2)*k   #Floor division returns integer answer
if total>n:
    print(total-n)
else:
    print("0")