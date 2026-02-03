a=input().split()
#n, k, l, c, d, p, nl, np,
n=int(a[0]) #number of friends
k=int(a[1]) #number of drinks 
l=int(a[2]) #number of mililitres of each bottle
c=int(a[3]) #number of limes
d=int(a[4]) #number of slices 
p=int(a[5]) #grams of salt
nl=int(a[6]) #each friend needs nl mililitres of drink for toast
np=int(a[7]) # grams of salt for each toast 

x=k*l #total_drink
y=c*d #total_slices
z=p  #total_salt

d1=x//nl #according to amount of drinks required per toast
l1=y//1 #according to amount  of slices required per toast
s1=z//np #according to amount of salt required per toast
  
m=min(d1,l1,s1)
toast=m//n
print(toast)


                      