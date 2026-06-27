def user_logic(N):
    MOD = 998244353

    dp = [1] * 10  # dp[d] = count of numbers ending with digit d
    dp[0] = 0      # digit 0 is not allowed

    for _ in range(2, N + 1):
        ndp = [0] * 10
        for d in range(1, 10):
            ndp[d] = dp[d]
            if d > 1:
                ndp[d] = (ndp[d] + dp[d - 1]) % MOD
            if d < 9:
                ndp[d] = (ndp[d] + dp[d + 1]) % MOD
        dp = ndp

    return sum(dp[1:]) % MOD


def main():
    import sys
    N = int(sys.stdin.read().strip())
    print(user_logic(N))


if __name__ == "__main__":
    main()