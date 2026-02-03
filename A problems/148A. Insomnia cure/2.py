import math

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

def count(x):
    return d // x

def lcm(a, b):
    return a * b // math.gcd(a, b)

# Inclusion–Exclusion Principle
ans = (
    count(k) + count(l) + count(m) + count(n)
    - count(lcm(k, l)) - count(lcm(k, m)) - count(lcm(k, n)) - count(lcm(l, m)) - count(lcm(l, n)) - count(lcm(m, n))
    + count(lcm(k, lcm(l, m))) + count(lcm(k, lcm(l, n))) + count(lcm(k, lcm(m, n))) + count(lcm(l, lcm(m, n)))
    - count(lcm(k, lcm(lcm(m, n), n)))  # lcm of all four
)

print(ans)
