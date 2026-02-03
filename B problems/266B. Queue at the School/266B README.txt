a = input().split()
Reads a line of input like "5 3" and splits it into a list of strings ['5', '3'].

This is needed because the problem gives n (number of children) and t (seconds) on the same line.

python
Copy code
n = int(a[0])
t = int(a[1])
Converts the strings from the split input into integers.

n is the length of the queue.

t is the number of seconds we need to simulate the swaps.

python
Copy code
x = input()
Reads the next line of input: the initial queue as a string, e.g., "BGGB".

python
Copy code
c = list(x)
Converts the string into a list of characters so that we can swap elements in place.

Strings in Python are immutable, so we can’t do x[i], x[i+1] = ... directly.

python
Copy code
for t in range(t):
Loops for each second of the simulation.

After each iteration, the queue c is updated according to the rules.

python
Copy code
    i = 0
    while i < n - 1:
Initializes an index i to 0 for each second.

while loop is used instead of for because we sometimes need to skip the next index after a swap.

If we used a for loop like for i in range(n-1), incrementing i inside the loop (i += 2) wouldn’t work as intended.

python
Copy code
        if c[i] == 'B' and c[i+1] == 'G':
Checks the rule: if a boy (B) has a girl (G) immediately after him, he should swap with her.

python
Copy code
            c[i], c[i+1] = c[i+1], c[i]
Performs the swap in place.

Python allows swapping two variables in one line without a temporary variable.

python
Copy code
            i += 2
After swapping, we skip the next index (i+1) because the B just moved forward.

This avoids accidentally swapping the same B again in the same second.

python
Copy code
        else:
            i += 1
If there’s no swap, move to the next position normally.

python
Copy code
print("".join(c))
Converts the list c back to a string for printing.

The output matches the problem’s required format.

✅ Key point about while vs for:

for loops in Python automatically increment i each iteration.

Here, after a swap, we need i += 2 to skip the next element.

If we used for, manually changing i inside the loop won’t affect the next iteration as intended.

while gives full control over i, so we can increment it by 1 or 2 depending on whether a swap happened.














Perfect! Let’s visualize a small example so you can see how the queue evolves and why i += 2 is necessary.

Example:

Input:

n = 5, t = 2
queue = B G B G G


Convert to list:

c = ['B', 'G', 'B', 'G', 'G']

Time = 1 second

We start with i = 0:

i = 0: c[0] = B and c[1] = G → swap

['G', 'B', 'B', 'G', 'G']


Now skip the next index → i = 2

i = 2: c[2] = B and c[3] = G → swap

['G', 'B', 'G', 'B', 'G']


Skip next → i = 4

i = 4: c[4] = G → no swap → i += 1 = 5 → exit while

Queue after 1 second:

G B G B G

Time = 2 seconds

Start again with i = 0:

i = 0: c[0] = G → no swap → i = 1

i = 1: c[1] = B, c[2] = G → swap

['G', 'G', 'B', 'B', 'G']


Skip next → i = 3

i = 3: c[3] = B, c[4] = G → swap

['G', 'G', 'B', 'G', 'B']


Skip next → i = 5 → exit while

Queue after 2 seconds:

G G B G B


✅ Key observation:

If we didn’t skip the next index (i += 2), the same B could swap twice in one second, which is not allowed by the rules.

The while loop allows flexible control over i depending on whether a swap happened.