MOD = 998244353

def count_valid_ways(cards):
    n = len(cards)

    # dp[i][0] = ways if card i shows front
    # dp[i][1] = ways if card i shows back
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = 1
    dp[0][1] = 1

    for i in range(1, n):
        a, b = cards[i]
        pa, pb = cards[i - 1]

        if a != pa:
            dp[i][0] = (dp[i][0] + dp[i - 1][0]) % MOD
        if a != pb:
            dp[i][0] = (dp[i][0] + dp[i - 1][1]) % MOD

        if b != pa:
            dp[i][1] = (dp[i][1] + dp[i - 1][0]) % MOD
        if b != pb:
            dp[i][1] = (dp[i][1] + dp[i - 1][1]) % MOD

    return (dp[-1][0] + dp[-1][1]) % MOD

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    cards = []
    index = 1
    for i in range(n):
        a = int(data[index])
        b = int(data[index + 1])
        cards.append((a, b))
        index += 2
    
    # Call user logic function and print the output
    result = count_valid_ways(cards)
    print(result)

if __name__ == "__main__":
    main()
