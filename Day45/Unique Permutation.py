def another_permutation_problem(nums, K):
    n = len(nums)
    return (n - 1 + (K - 2)) // (K - 1)


def main():
    import sys
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    nums = list(map(int, data[1:n + 1]))
    K = int(data[n + 1])

    print(another_permutation_problem(nums, K))


if __name__ == "__main__":
    main()