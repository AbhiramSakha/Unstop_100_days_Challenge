def palindrome_phobia(n, s):
    MOD = 10**9 + 7
    from functools import lru_cache

    @lru_cache(None)
    def dp(pos, last1, last2, tight, bigger):
        if pos == n:
            return 1 if bigger else 0

        start = ord(s[pos]) - ord('a') if tight else 0
        ans = 0

        for c in range(start, 26):
            if last1 != 26 and c == last1:
                continue
            if last2 != 26 and c == last2:
                continue

            ntight = tight and (c == start)
            nbigger = bigger or (tight and c > start)

            ans = (ans + dp(pos + 1, c, last1, ntight, nbigger)) % MOD

        return ans

    return dp(0, 26, 26, 1, 0)


def main():
    import sys
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    s = data[1]

    print(palindrome_phobia(n, s))

if __name__ == "__main__":
    main()