def process_test_case(N, Q, A, queries):
    result = []

    size = 1
    while size < N:
        size *= 2

    seg = [0] * (2 * size)

    for i in range(N):
        seg[size + i] = A[i]

    for i in range(size - 1, 0, -1):
        seg[i] = max(seg[2 * i], seg[2 * i + 1])

    for typ, data in queries:
        if typ == 1:
            result.append(seg[1])
        else:
            idx, val = data
            pos = size + idx - 1
            seg[pos] = val

            pos //= 2
            while pos:
                seg[pos] = max(seg[2 * pos], seg[2 * pos + 1])
                pos //= 2

    return result


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N, Q = map(int, input().split())
        A = list(map(int, input().split()))

        queries = []
        for _ in range(Q):
            query = input().split()
            if query[0] == '?':
                queries.append((1, (0, 0)))
            else:
                x, y = int(query[1]), int(query[2])
                queries.append((0, (x, y)))

        result = process_test_case(N, Q, A, queries)

        for res in result:
            print(res)