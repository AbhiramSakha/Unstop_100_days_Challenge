def can_form_by_interleaving(S, T):
    if len(S) != len(T):
        return False

    n = len(S)
    mid = n // 2
    a = S[:mid]
    b = S[mid:]

    if len(a) + len(b) != len(T):
        return False

    m, k = len(a), len(b)

    dp = [[False] * (k + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for i in range(m + 1):
        for j in range(k + 1):
            if i > 0 and dp[i - 1][j] and a[i - 1] == T[i + j - 1]:
                dp[i][j] = True
            if j > 0 and dp[i][j - 1] and b[j - 1] == T[i + j - 1]:
                dp[i][j] = True

    return dp[m][k]

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    S = data[0]  # First input string
    T = data[1]  # Second input string
    
    # Call user logic function and print the output
    result = can_form_by_interleaving(S, T)
    print(1 if result else 0)

if __name__ == "__main__":
    main()