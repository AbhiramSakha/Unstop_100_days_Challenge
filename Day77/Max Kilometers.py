def solve(A, B, C, D):
    # Minimum petrol needed (all hybrid)
    min_petrol = B * D

    # Must end with strictly positive petrol
    if min_petrol >= A:
        return -1

    # Extra petrol available beyond all-hybrid travel
    extra = A - 1 - min_petrol

    # Each petrol-only km consumes (C - D) extra litres
    x = extra // (C - D)

    return min(B, x)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    A = int(data[0])
    B = int(data[1])
    C = int(data[2])
    D = int(data[3])

    result = solve(A, B, C, D)
    print(result)


if __name__ == "__main__":
    main()