def longest_subsequence(s):
    dp = [0] * 26

    for ch in s:
        cur = ord(ch) - ord('a')
        best = 0

        for prev in range(26):
            if abs(prev - cur) != 1:
                best = max(best, dp[prev])

        dp[cur] = max(dp[cur], best + 1)

    return max(dp)

def main():
    import sys
    input = sys.stdin.read
    s = input().strip()

    result = longest_subsequence(s)
    print(result)

if __name__ == "__main__":
    main()