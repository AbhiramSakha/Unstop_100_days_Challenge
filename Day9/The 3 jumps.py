def min_cost_to_end(N, V):
    dp = [float('inf')] * N
    dp[0] = 0  # Starting point

    for i in range(1, N):
        for j in range(1, 4):  # Steps: 1, 2, 3
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + abs(V[i] - V[i - j]))
    
    return dp[N - 1]

# Reading input
N = int(input())
V = list(map(int, input().split()))

# Calculating and printing result
print(min_cost_to_end(N, V))
                            