from itertools import permutations

def count_divisible_combinations(K, N, arr):
    nums = set()

    for length in range(1, N + 1):
        for p in permutations(arr, length):
            num = int(''.join(map(str, p)))

            if num % K == 0:
                nums.add(num)

    return len(nums)

if __name__ == '__main__':
    K = int(input())
    N = int(input())
    arr = list(map(int, input().split()))

    result = count_divisible_combinations(K, N, arr)
    print(result)