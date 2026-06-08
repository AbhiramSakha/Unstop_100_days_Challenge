def can_partition_chocolates(n, chocolates):
    total = sum(chocolates)

    if total % 2:
        return "NO"

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for x in chocolates:
        for s in range(target, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]

    return "YES" if dp[target] else "NO"


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    chocolates = list(map(int, data[1:]))

    result = can_partition_chocolates(n, chocolates)
    print(result)

if __name__ == "__main__":
    main()