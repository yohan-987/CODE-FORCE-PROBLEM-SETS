t=int(input())
for i in range(t):
    a=input()
    b=''.join(sorted(a))
    if "YY" in b:
        print("NO")
    elif "YY" in a:
        print("NO")
    else:
        print("YES")
