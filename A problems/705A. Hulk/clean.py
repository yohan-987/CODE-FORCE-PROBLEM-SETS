n = int(input())

phrases = []
for i in range(n):
    if i % 2 == 0:
        phrases.append("I hate")
    else:
        phrases.append("I love")

# Join with " that " and add " it" at the end
result = " that ".join(phrases) + " it"
print(result)
