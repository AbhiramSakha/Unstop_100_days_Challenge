def minSwapsCouples(arr):
    pos = {person: i for i, person in enumerate(arr)}
    swaps = 0

    for i in range(0, len(arr), 2):
        first = arr[i]
        partner = first ^ 1

        if arr[i + 1] != partner:
            partner_pos = pos[partner]

            pos[arr[i + 1]] = partner_pos
            arr[partner_pos] = arr[i + 1]

            arr[i + 1] = partner
            pos[partner] = i + 1

            swaps += 1

    return swaps


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = minSwapsCouples(arr)
    print(result)