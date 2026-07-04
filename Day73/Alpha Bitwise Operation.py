def alpha_bitwise_operation(n, arr):
    result = 0

    if n == 0:
        return 0

    max_bits = max(arr).bit_length()
    if max_bits == 0:
        return 0

    for bit in range(max_bits):
        cnt = 0
        mask = 1 << bit
        for num in arr:
            if num & mask:
                cnt += 1

        if cnt * 2 > n:      # strictly greater than half
            result |= mask

    return result


def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))

    n = data[0]
    arr = data[1:]

    print(alpha_bitwise_operation(n, arr))

if __name__ == "__main__":
    main()