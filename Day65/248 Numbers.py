MOD = 1000000007

def count_248_numbers(N):
    s = str(N)
    n = len(s)

    from functools import lru_cache

    OFFSET = 8 

    @lru_cache(None)
    def dp(pos, diff24, diff28, has2, started, tight):
        if pos == n:
            return 1 if started and diff24 == OFFSET and diff28 == OFFSET and has2 else 0

        limit = int(s[pos]) if tight else 9
        ans = 0

        for d in range(limit + 1):
            ntight = tight and (d == limit)

            if not started and d == 0:
                ans += dp(pos + 1, diff24, diff28, has2, False, ntight)
            else:
                nd24 = diff24
                nd28 = diff28
                nhas2 = has2

                if d == 2:
                    nd24 += 1
                    nd28 += 1
                    nhas2 = True
                elif d == 4:
                    nd24 -= 1
                elif d == 8:
                    nd28 -= 1

                if 0 <= nd24 <= 16 and 0 <= nd28 <= 16:
                    ans += dp(pos + 1, nd24, nd28, nhas2, True, ntight)

        return ans % MOD

    return dp(0, OFFSET, OFFSET, False, False, True)


def main():
    import sys
    N = int(sys.stdin.read().strip())
    print(count_248_numbers(N))

if __name__ == "__main__":
    main()