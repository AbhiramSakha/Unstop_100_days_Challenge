import math

def find_smallest_multiple(P, N):
    return (P * N) // math.gcd(P, N)

# Input
P, N = map(int, input().split())

# Output
print(find_smallest_multiple(P, N))