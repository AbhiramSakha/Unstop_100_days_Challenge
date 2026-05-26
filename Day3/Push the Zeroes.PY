def push_zeroes_to_end(arr):
    n = len(arr)
    index = 0  # Points to the position for the next non-zero element

    # Move non-zero elements forward
    for i in range(n):
        if arr[i] != 0:
            arr[index] = arr[i]
            index += 1

    # Fill remaining elements with zero
    while index < n:
        arr[index] = 0
        index += 1

    return arr

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    
    result = push_zeroes_to_end(arr)
    print(*result)