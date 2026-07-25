def trap_rain_water(n, arr):
    left = 0
    right = n - 1
    left_max = 0
    right_max = 0
    water = 0

    while left <= right:
        if arr[left] <= arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                water += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                
                right_max = arr[right]
            else:
                water += right_max - arr[right]
            right -= 1

    return water


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(trap_rain_water(n, arr))


if __name__ == "__main__":
    main()