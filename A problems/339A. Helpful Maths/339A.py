s = input() #Takes the string
nums = s.split('+') #spilt the string in such a way that there won't be a plus
b = sorted(nums)  # returns a new sorted list
c = "+".join(b)   #Opposite of split function 
print(c)

       