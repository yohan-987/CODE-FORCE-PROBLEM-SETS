t=int(input())
for i in range(t):
    a=int(input())
    if a%2==0 or a%3==0:
        print(a)
    else:
        b=abs((a-3)-3)
        print(b)