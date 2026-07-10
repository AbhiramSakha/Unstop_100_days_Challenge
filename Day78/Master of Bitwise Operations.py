def user_logic(n, q, arr, queries):
    # prefix[bit][i] = number of elements having 'bit' set
    # in the first i elements (bits are 0 to 29)
    prefix = [[0] * (n + 1) for _ in range(30)]

    for b in range(30):
        for i in range(1, n + 1):
            prefix[b][i] = prefix[b][i - 1] + ((arr[i - 1] >> b) & 1)

    ans = []

    for k, X1, Y1, X2, Y2 in queries:
        b = k

        ones1 = prefix[b][Y1] - prefix[b][X1 - 1]
        len1 = Y1 - X1 + 1
        zeros1 = len1 - ones1

        ones2 = prefix[b][Y2] - prefix[b][X2 - 1]
        len2 = Y2 - X2 + 1
        zeros2 = len2 - ones2

        ans.append(ones1 * zeros2 + zeros1 * ones2)

    return ans


def main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0

    T = data[idx]
    idx += 1

    out = []

    for _ in range(T):
        n = data[idx]
        q = data[idx + 1]
        idx += 2

        arr = data[idx:idx + n]
        idx += n

        queries = []
        for _ in range(q):
            queries.append(data[idx:idx + 5])
            idx += 5

        out.extend(map(str, user_logic(n, q, arr, queries)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()