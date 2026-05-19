def peakIndexInMountainArray(arr):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < arr[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(peakIndexInMountainArray(arr))