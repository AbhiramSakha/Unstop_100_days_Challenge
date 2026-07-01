MOD = 10**9 + 7

def user_logic(N):
    if N == 0:
        return "1"

    # Count of strings ending with a, e, i, o, u
    a = e = i = o = u = 1

    for _ in range(2, N + 1):
        na = (e + u) % MOD
        ne = (a + i) % MOD
        ni = (e + o) % MOD
        no = (i + u) % MOD
        nu = (a + o) % MOD
        a, e, i, o, u = na, ne, ni, no, nu

    total = (a + e + i + o + u) % MOD

    if total == 0:
        return "1"

    return oct(total)[2:]


def main():
    import sys
    input = sys.stdin.read
    data = input().strip()

    N = int(data)

    result = user_logic(N)
    print(result)


if __name__ == "__main__":
    main()