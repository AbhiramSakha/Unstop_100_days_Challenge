def maximizeNutritionalValue(n, m, k, price, nutrition):
    NEG = -10**18

    dp = [[NEG] * (m + 1) for _ in range(k + 1)]
    dp[0][0] = 0

    for i in range(n):
        ndp = [row[:] for row in dp]

        normal = price[i]
        discount = price[i] // 2

        for used in range(k + 1):
            for cost in range(m + 1):
                if dp[used][cost] == NEG:
                    continue

                if cost + normal <= m:
                    ndp[used][cost + normal] = max(
                        ndp[used][cost + normal],
                        dp[used][cost] + nutrition[i]
                    )

                if used < k and cost + discount <= m:
                    ndp[used + 1][cost + discount] = max(
                        ndp[used + 1][cost + discount],
                        dp[used][cost] + nutrition[i]
                    )

        dp = ndp

    ans = 0
    for used in range(k + 1):
        ans = max(ans, max(dp[used]))

    return ans
if __name__ == "__main__":
    n, m, k = map(int, input().split())
    price = list(map(int, input().split()))
    nutrition = list(map(int, input().split()))
    result = maximizeNutritionalValue(n, m, k, price, nutrition)
    print(result)