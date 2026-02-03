n = int(input())
b = input().upper()  # string of game results

a = b.count("A")  # count Anton's wins
d = b.count("D")  # count Danik's wins

if a > d:
    print("Anton")
elif d > a:
    print("Danik")
else:
    print("Friendship")
