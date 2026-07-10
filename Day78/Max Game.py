def user_logic(n, q, arr, queries):
    size = 1
    while size < n:
        size <<= 1

    seg = [0] * (2 * size)

    # Build
    for i in range(n):
        seg[size + i] = arr[i]
    for i in range(size - 1, 0, -1):
        seg[i] = max(seg[2 * i], seg[2 * i + 1])

    results = []

    for query in queries:
        if query[0] == 1:
            _, l, r = query
            l += size
            r += size
            ans = 0

            while l <= r:
                if l & 1:
                    ans = max(ans, seg[l])
                    l += 1
                if not (r & 1):
                    ans = max(ans, seg[r])
                    r -= 1
                l //= 2
                r //= 2

            results.append(ans)

        else:
            _, idx, val = query
            pos = size + idx
            seg[pos] = val
            pos //= 2

            while pos:
                seg[pos] = max(seg[2 * pos], seg[2 * pos + 1])
                pos //= 2

    return results


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    q = int(data[1])
    arr = list(map(int, data[2:n + 2]))

    queries = []
    idx = n + 2

    for _ in range(q):
        t = int(data[idx])
        a = int(data[idx + 1])
        b = int(data[idx + 2])
        queries.append((t, a, b))
        idx += 3

    results = user_logic(n, q, arr, queries)

    print(*results, sep="\n")


if __name__ == "__main__":
    main()