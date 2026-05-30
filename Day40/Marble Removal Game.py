def remove_marbles(n, k, sequence):
    dp = [0] * (n + 1)

    for marbles in range(1, n + 1):
        best = 0

        for move in sequence:
            if move <= marbles:
                best = max(best, move + (marbles - move - dp[marbles - move]))

        dp[marbles] = best

    return dp[n]

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    k = int(data[1])

    sequence = list(map(int, data[2:2 + k]))

    result = remove_marbles(n, k, sequence)
    print(result)

if __name__ == "__main__":
    main()