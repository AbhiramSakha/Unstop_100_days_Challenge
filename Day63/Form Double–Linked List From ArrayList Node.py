# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
m = int(input())

mat = [list(map(int, input().split())) for _ in range(n)]

result = []

# Even-indexed rows first (0, 2, 4, ...)
for i in range(0, n, 2):
    result.extend(mat[i])

# Odd-indexed rows next (1, 3, 5, ...)
for i in range(1, n, 2):
    result.extend(mat[i])

for x in result:
    print(f"{x} <---> ", end="")

print("null")