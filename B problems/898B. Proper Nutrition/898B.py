n=int(input())
a=int(input()) #cost of one Cola 
b=int(input()) #cost of one bars


#we float division because normal division will give decimals 

#assume we buy x cola bottles , money spend 
for x in range(n//a+1):   # n//a+1 becuase it is max no of cola we could buy theoritically 
    rem=n-(x*a)    #remaining money after buy x Cola 
    if rem%b==0 and rem>=0:
        y=rem//b   #is rem is divisble by b then total number of bars we could buy 
        print("YES")
        print(x,y)
        break   
else:             
    print("NO")    
 
'''
    else outside of the loop  because we need to
    check x until we found one valid case 
    but if else is inside it will stop in invalid cases 
    and won't find the right one 


'''