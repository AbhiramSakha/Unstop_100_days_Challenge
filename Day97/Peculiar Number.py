def peculiarNumber(n, k, arr):
    arr = [abs(arr[i] - i) for i in range(n)]

    def can(limit):
        parts = 1
        curr = 0
        for x in arr:
            if curr + x <= limit:
                curr += x
            else:
                parts += 1
                curr = x
        return parts <= k

    low = max(arr)
    high = sum(arr)

    while low < high:
        mid = (low + high) // 2
        if can(mid):
            high = mid
        else:
            low = mid + 1

    x = low

    if x >= 100:
        return x

    a, b = 0, 1
    for _ in range(x):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(peculiarNumber(n, k, arr))