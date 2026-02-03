n=[]
for i in range(5):
    r=list(map(int,input().split()))
    n.append(r)
for i in range(5):
    for j in range(5):
        if n[i][j] == 1:
            print(abs(i - 2) + abs(j - 2))    #abs works like mod |x-1| , and 2 because index starts from 0
            break