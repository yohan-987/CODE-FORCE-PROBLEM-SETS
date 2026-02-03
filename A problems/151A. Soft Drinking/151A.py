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

#for absolute maximum toast 
d1=x//nl #according to amount of drinks 
_d1=0
l1=y #according to amount  of slices
_l1=0
s1=z//np #according to amount of salt
_s1=0
if d1<l1 and d1<s1:
      _d1+=1
elif l1<d1 and l1<s1:
      _l1+=1
else:
      _s1+=1
if _d1==1:
      m=d1
      j=m//n
      print(j)
elif _l1==1:
      m=l1
      j=m//n
      print(j)
else:
      m=s1
      j=m//n
      print(j)

                      