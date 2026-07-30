def user_logic(N, X, prices, durations):
    dp = [0] * (X + 1)

    for i in range(N):
        cost = prices[i]
        value = durations[i]
        for j in range(X, cost - 1, -1):
            dp[j] = max(dp[j], dp[j - cost] + value)

    return dp[X]

if __name__ == "__main__":
    N, X = map(int, input().split())
    prices = list(map(int, input().split()))
    durations = list(map(int, input().split()))
    result = user_logic(N, X, prices, durations)
    print(result)