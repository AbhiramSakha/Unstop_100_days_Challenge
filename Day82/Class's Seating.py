def calculate_k_values(n, m, seat_populations):
    total = sum(seat_populations)

    min_k = max(
        max(seat_populations),
        (total + m + n - 1) // n
    )

    max_k = max(seat_populations) + m

    return min_k, max_k


def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))

    n = data[0]
    m = data[1]
    seat_populations = data[2:2+n]

    mn, mx = calculate_k_values(n, m, seat_populations)
    print(mn, mx)


if __name__ == "__main__":
    main()