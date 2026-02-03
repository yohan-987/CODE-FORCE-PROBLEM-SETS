p=input().split()
n=int(p[0])
m=int(p[1])
a=int(p[2])
q=((n+a-1)//a)*((m+a-1)//a)
print(q)
'''
A1/A2 = wrong = because sometimes tiles can't cover the 
square properly and we can't cut the tiles 

n/a = gives number of tiles to be put in dimension of n 
but eg.= 10/3=3.33 , we can't put 3.33 tiles so we need 4 tiles 
10//3=3 wrong , 10//3+1 = 4 right but wrong for other cases 

eg= 12//3 +1 =5 wrong(we can cover completely with 4)

for new formula = (n+a-1)//a
'''