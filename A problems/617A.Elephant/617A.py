x=int(input())
jumps_5 = x//5 #full 5 steps , // is floor division , eg , 12 steps means two 5 full steps , 12//5=2
r=x%5  #remainder , it would be less than  5 
# eg 12//5=2 , two time 5 steps then only 2 unit distance would be left and which can be covered by one 2 steps
if r==0:
   print(jumps_5)
else:
   print(jumps_5 + 1)   