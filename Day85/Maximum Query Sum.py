import sys


def user_logic(n, q, arr, queries):
    # Prefix sum
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    ans = []

    for l, idx, r in queries:
        # Sum from l to idx-1
        left_sum = prefix[idx] - prefix[l]

        # Sum from idx+1 to r
        right_sum = prefix[r + 1] - prefix[idx + 1]

        res = left_sum * right_sum

        if res < 0:
            res = 0

        ans.append(res)

    return ans


def main():
    input = sys.stdin.readline

    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    queries = []
    for _ in range(q):
        l, idx, r = map(int, input().split())
        queries.append((l, idx, r))

    results = user_logic(n, q, arr, queries)

    print("\n".join(map(str, results)))


if __name__ == "__main__":
    main()