n = int(input())
a = input().split()

c = []
for k in range(n):
    c.append(int(a[k]))

for j in range(n):
    for i in range(0, n - j - 1):
        if c[i] > c[i + 1]:
            c[i], c[i + 1] = c[i + 1], c[i]

print(*c)
      
