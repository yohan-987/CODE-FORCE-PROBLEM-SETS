n = input().strip()
num = int(n)

# Generate all lucky numbers up to 1000 (or you can extend the range)
lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

# Check if n itself is made of only 4s and 7s (purely lucky)
if all(ch in '47' for ch in n):
    lucky_numbers.append(num)

# If divisible by any lucky number -> YES
for lucky in lucky_numbers:
    if num % lucky == 0:
        print("YES")
        break
else:
    print("NO")
