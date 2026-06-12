def can_select_people(N, K, arr):
    dp = [False] * (K + 1)
    dp[0] = True

    for num in arr:
        for s in range(K, num - 1, -1):
            if dp[s - num]:
                dp[s] = True

    return "YES" if dp[K] else "NO"


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    N = int(data[0])
    K = int(data[1])
    arr = list(map(int, data[2:2 + N]))

    result = can_select_people(N, K, arr)
    print(result)

if __name__ == "__main__":
    main()