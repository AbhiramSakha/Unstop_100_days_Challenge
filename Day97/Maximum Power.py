def can_partition(arr):
    total = sum(arr)
    if total % 2:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in arr:
        for s in range(target, num - 1, -1):
            if dp[s - num]:
                dp[s] = True

    return dp[target]


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    if can_partition(arr):
        print(sum(arr) // 2)
    else:
        print(0)