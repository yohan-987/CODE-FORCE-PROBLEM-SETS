n=int(input())
o=input().split()
d=list(map(int,o))
s=0
for i in range(n):
    s=s+d[i]
print(100*(s/(100*n))) #percentage , total orange/total cocktailṇ