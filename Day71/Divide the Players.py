def divide_players(arr, n, k):
    total = sum(arr)
    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for num in arr:
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]

    best = 0
    for s in range(target, -1, -1):
        if dp[s]:
            best = s
            break

    return abs(total - 2 * best)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    answer = divide_players(arr, n, k)
    if answer <= k:
        print("True")
    else:
        print("False")