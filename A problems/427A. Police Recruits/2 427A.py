n = int(input())
a = input().split()   # read space-separated values
free = 0
untreated = 0

for i in a:
    i = int(i)        # manually convert each string to int
    if i == -1:
        if free > 0:     #it will check if a police is already free or not 
            free -= 1    #officer will investigate it , no increament in untreated crime
        else:
            untreated += 1  #no officer means untreated crime
    else:
        free += i   #its officer not crime alert so the officer gets recruited 

print(untreated)
