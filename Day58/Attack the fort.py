def calculate_difference(arr):
    positives = {x for x in arr if x > 0}

    if not positives:
        return -1

    max_power = max(arr)

    best_len = 0
    best_end = float('inf')

    for x in positives:
        if x - 1 not in positives:  # start of a consecutive chain
            cur = x
            length = 1

            while cur + 1 in positives:
                cur += 1
                length += 1

            end = cur

            if length > best_len:
                best_len = length
                best_end = end
            elif length == best_len:
                best_end = min(best_end, end)

    return abs(max_power - (best_end + 1))


def main():
    import sys
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    arr = list(map(int, data[1:n + 1]))

    print(calculate_difference(arr))


if __name__ == "__main__":
    main()