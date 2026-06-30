def minimumCost(N, S, time, cost):
    # Step 1: Compute prefix sums for O(1) range sum queries
    pref_time = [0] * (N + 1)
    pref_cost = [0] * (N + 1)
    
    for i in range(N):
        pref_time[i + 1] = pref_time[i] + time[i]
        pref_cost[i + 1] = pref_cost[i] + cost[i]
        
    # Step 2: Initialize DP table with infinity
    dp = [float('inf')] * (N + 1)
    dp[0] = 0  # Base case: 0 cost for 0 items
    
    # Step 3: Fill the DP table
    for i in range(1, N + 1):
        for j in range(i):
            # Calculate the cost added by making a batch from j+1 to i
            current_cost = dp[j] + (S + pref_time[i] - pref_time[j]) * (pref_cost[N] - pref_cost[j])
            if current_cost < dp[i]:
                dp[i] = current_cost
                
    return dp[N]

if __name__ == "__main__":
    N, S = map(int, input().split())
    time = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    print(minimumCost(N, S, time, cost))
