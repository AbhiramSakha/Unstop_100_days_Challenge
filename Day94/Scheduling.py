def min_difficulty(arr, d):
    n = len(arr)
    if n < d:
        return -1

    INF = float('inf')
    dp = [[INF] * n for _ in range(d)]

    mx = 0
    for i in range(n):
        mx = max(mx, arr[i])
        dp[0][i] = mx

    for day in range(1, d):
        for i in range(day, n):
            mx = 0
            for j in range(i, day - 1, -1):
                mx = max(mx, arr[j])
                dp[day][i] = min(dp[day][i], dp[day - 1][j - 1] + mx)

    return dp[d - 1][n - 1]


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    B = int(data[0])
    arr = list(map(int, data[1:B + 1]))
    D = int(data[B + 1])

    result = min_difficulty(arr, D)
    print(result)


if __name__ == "__main__":
    main()