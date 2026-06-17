# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
arr = list(map(int, input().split()))

res = [arr[0]]

for i in range(1, n):
    if arr[i] != arr[i - 1]:
        res.append(arr[i])

print(*res)

