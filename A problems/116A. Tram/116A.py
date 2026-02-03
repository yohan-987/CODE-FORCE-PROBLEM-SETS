n=int(input())
exit=[]
enter=[]
for j in range(n):
    a=input().split()
    exit.append(int(a[0]))
    enter.append(int(a[1]))
current=0
max=0
for i in range(n):
    current=current+enter[i]-exit[i]
    if current>max:
          max=current
print(max)          


'''
| Stop | Exit | Enter | Current | Max |
| ---- | ---- | ----- | ------- | --- |
| 1    | 0    | 3     | 0-0+3=3 | 3   |
| 2    | 2    | 5     | 3-2+5=6 | 6   |
| 3    | 4    | 2     | 6-4+2=4 | 6   |
| 4    | 4    | 0     | 4-4+0=0 | 6   |
 '''