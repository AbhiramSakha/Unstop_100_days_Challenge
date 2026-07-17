from bisect import bisect_left

def max_subarray_sum_modified_list(n, first_list, second_list):
    sorted_second = sorted(second_list)

    modified = []

    for x in first_list:
        idx = bisect_left(sorted_second, x)

        if idx < n and sorted_second[idx] == x:
            modified.append(sorted_second[(idx + 1) % n])
        else:
            modified.append(x)

    # Kadane
    best = cur = modified[0]
    for i in range(1, n):
        cur = max(modified[i], cur + modified[i])
        best = max(best, cur)

    return best


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    first_list = list(map(int, data[1:n + 1]))
    second_list = list(map(int, data[n + 1:2 * n + 1]))

    result = max_subarray_sum_modified_list(n, first_list, second_list)
    print(result)


if __name__ == "__main__":
    main()