def user_logic(n, d):
    MOD = 998244353

    pow_d_plus = pow(2, d + 1, MOD)
    pow_d_minus = pow(2, d - 1, MOD) if d > 0 else 1

    inv2 = (MOD + 1) // 2
    nodes = pow(2, n - 1, MOD)

    ans = 0

    for h in range(n):
        contrib = 0

        if d <= h:
            contrib += pow_d_plus

        l = max(1, d - h)
        r = min(h, d - 1)

        if l <= r:
            contrib += (r - l + 1) * pow_d_minus

        ans = (ans + nodes * (contrib % MOD)) % MOD
        nodes = (nodes * inv2) % MOD

    return ans


def main():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    d = data[1]

    print(user_logic(n, d))


if __name__ == "__main__":
    main()