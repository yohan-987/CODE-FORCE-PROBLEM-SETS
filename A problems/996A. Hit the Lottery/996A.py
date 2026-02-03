n = int(input())
# 1, 5, 10, 20, 100
a = [1, 5, 10, 20, 100]
c = 0

while n > 0:  # because we need to freedom in change of n
    
    if n >= 100:
        c += 1
        n -= 100   #  subtract
    if 100> n >= 20:
        c += 1
        n -= 20
    if 20> n >= 10:
        c += 1
        n -= 10
    if 10> n >= 5:
        c += 1
        n -= 5
    if 5>n>=1:
        c += 1
        n -= 1

print(c)
