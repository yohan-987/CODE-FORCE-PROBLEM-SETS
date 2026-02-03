n = int(input())
c = input()[:n]
count = 0
for i in range(n-1):
    if c[i] == c[i+1]:
        count += 1
print(count)
