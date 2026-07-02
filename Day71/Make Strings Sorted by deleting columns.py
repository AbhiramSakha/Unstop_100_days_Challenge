def solve(strs):
    n = len(strs)
    m = len(strs[0])

    dp = [1] * m

    for j in range(m):
        for i in range(j):
            valid = True
            for s in strs:
                if s[i] > s[j]:
                    valid = False
                    break
            if valid:
                dp[j] = max(dp[j], dp[i] + 1)

    return m - max(dp)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    strs = data[1:n + 1]

    print(solve(strs))

if __name__ == "__main__":
    main()