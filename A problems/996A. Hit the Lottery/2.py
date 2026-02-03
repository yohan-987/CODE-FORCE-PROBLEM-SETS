n = int(input())
c = 0

while n > 0:
    if n >= 100:
        c += 1
        n -= 100
    elif n >= 20:
        c += 1
        n -= 20
    elif n >= 10:
        c += 1
        n -= 10
    elif n >= 5:
        c += 1
        n -= 5
    else:
        c += 1
        n -= 1

print(c)


#elif condition is only checked when previous ones are all false 