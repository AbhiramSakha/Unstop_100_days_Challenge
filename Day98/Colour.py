MOD = 998244353


def nCr_mod(n, r, fact, inv_fact):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD


def user_logic(n, m, k, edges):
    """
    Number of colorings with exactly K red vertices
    such that number of edges between different colors is even.
    """


    deg = [0] * (n + 1)

    for u, v in edges:
        deg[u] ^= 1
        deg[v] ^= 1

    odd_vertices = []
    even_vertices = []

    for i in range(1, n + 1):
        if deg[i]:
            odd_vertices.append(i)
        else:
            even_vertices.append(i)

    odd = len(odd_vertices)
    even = len(even_vertices)

    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD

    inv_fact = [1] * (n + 1)
    inv_fact[n] = pow(fact[n], MOD - 2, MOD)

    for i in range(n, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    ans = 0

    for take_odd in range(0, min(odd, k) + 1, 2):
        take_even = k - take_odd

        if 0 <= take_even <= even:
            ans += (
                nCr_mod(odd, take_odd, fact, inv_fact)
                * nCr_mod(even, take_even, fact, inv_fact)
            )
            ans %= MOD

    return ans


def main():
    import sys

    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    m = int(data[1])
    k = int(data[2])

    edges = []
    index = 3

    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2

    result = user_logic(n, m, k, edges)
    print(result)


if __name__ == "__main__":
    main()