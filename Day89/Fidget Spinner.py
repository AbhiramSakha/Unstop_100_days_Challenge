MOD = 1000000007

def ways(sum):
    """
    Write your logic here.
    Parameters:
        sum (int): The target sum to construct
    Returns:
        int: Number of ways to construct the sum, modulo 10^9+7
    """
    dp = [0] * (sum + 1)
    dp[0] = 1

    for i in xrange(1, sum + 1):
        for j in xrange(1, 7):
            if i >= j:
                dp[i] = (dp[i] + dp[i - j]) % MOD

    return dp[sum]

def main():
    import sys
    input = sys.stdin.read
    data = input().strip()

    n = int(data)

    result = ways(n)
    print result

if __name__ == "__main__":
    main()