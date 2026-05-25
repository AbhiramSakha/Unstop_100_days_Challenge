def numSubarrayBoundedMax(A, L, R):
    ans = 0
    last_invalid = -1
    last_valid = -1

    for i, num in enumerate(A):
        if num > R:
            last_invalid = i

        if L <= num <= R:
            last_valid = i

        ans += max(0, last_valid - last_invalid)

    return ans

if __name__ == "__main__":
    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    print(numSubarrayBoundedMax(arr, l, r))
                          