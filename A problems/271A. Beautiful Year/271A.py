n=int(input())

for i in range(10000):
     c=[]
     n+=1
     b=str(n)
     for i in b:
          if i not in c:
               c.append(i)
     if len(c)==4:
          break
print("".join(c))