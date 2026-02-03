a=input()
if a=="{}":
    print("0")
else:
  b=a.strip("{}")
  x=b.split(",")
  c = []
  for i in x:
     clean_x = i.strip()   # remove spaces around each item
     c.append(clean_x)
  print(len(set(c)))