t=int(input())
d=[]
for i in range(t):
    n=int(input())
    a=input().split()
    b=input().split()
    c=input().split()
    a1=0  #scores
    b1=0
    c1=0
    frequency={}   #creating dictionary
    for w in a+b+c:   #checking words in all inputs , a b c are lists so they won't join like strings so can be obtained easily by index
        if w in frequency:       # if key already exists
            frequency[w] += 1    #Add the value
        else:               # if key does not exist
            frequency[w] = 1    #key and value are getting added simultaneously 
        '''
frequency is like
a = ["dog"]
b = ["cat"]
c = ["dog"]
The dictionary becomes:

python
Copy code
{"dog": 2, "cat": 1}
        '''
     # Scoring
    for i in range(n):
        # A
        if frequency[a[i]] == 1:
            a1 += 3
        elif frequency[a[i]] == 2:
            a1 += 1

        # B
        if frequency[b[i]] == 1:
            b1 += 3
        elif frequency[b[i]] == 2:
            b1 += 1

        # C
        if frequency[c[i]] == 1:
            c1 += 3
        elif frequency[c[i]] == 2:
            c1 += 1

    d.append([a1,b1,c1])

for x in d:
    print(*x)
