def calculate_difference(num):
    digits = list(str(abs(num)))

    if num >= 0:
        mx = int("".join(sorted(digits, reverse=True)))
        mn = int("".join(sorted(digits)))
    else:
        mx = -int("".join(sorted(digits)))
        mn = -int("".join(sorted(digits, reverse=True)))

    return mx - mn

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    T = int(data[0])
    results = []

    for i in range(1, T + 1):
        num = int(data[i])
        results.append(calculate_difference(num))

    print("\n".join(map(str, results)))


if __name__ == "__main__":
    main()