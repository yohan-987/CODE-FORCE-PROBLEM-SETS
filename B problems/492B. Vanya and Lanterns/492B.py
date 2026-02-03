a=list(map(int,input().split()))
b=sorted(list(map(int,input().split())))
d=[]
if a[0]>1:
  for i in range(a[0]-1):
    x=b[i+1]-b[i]  #Gap between to lamps 
    d.append(x)
  c=max(d)/2 # max Gap /2 , with this much their light can cover  for each other

#checking the start of street -> wasn't counted in loop 
  s=b[0]
#checking the end of street
  e=(a[1]-b[-1])
#min. radius of light to cover every street , if we can cover the largest of three of them , we can say every lamp can cover the street 
  y=max(c,s,e)
  print(y)
else:
  l=b[0]
  r=a[1]-b[0]
  y=max(l,r)
  print(y)

