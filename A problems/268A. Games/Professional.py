n = int(input())
home = []
away = []

for _ in range(n):
    h, a = map(int, input().split())
    home.append(h)
    away.append(a)

counter = sum(1 for i in range(n) for j in range(n) if home[i] == away[j])
print(counter)
