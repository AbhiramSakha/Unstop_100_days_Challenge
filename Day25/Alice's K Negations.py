# Enter your code here. Read input from STDIN. Print output to STDOUT
def maxPrizeMoney(n, k, arr):
    arr.sort()

    i = 0

    while i < n and k > 0 and arr[i] < 0:
        arr[i] = -arr[i]
        i += 1
        k -= 1

    total = sum(arr)

    if k % 2 == 1:
        total -= 2 * min(arr)

    return total


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    print(maxPrizeMoney(n, k, arr))