def is_valid(sequence):
    prefix_sum = 0
    for num in sequence:
        prefix_sum += num
        if prefix_sum == 0:
            return False
    return True

N = int(input())
arr = list(map(int, input().split()))

desc = sorted(arr, reverse=True)
asc = sorted(arr)

valid_desc = is_valid(desc)
valid_asc = is_valid(asc)

if valid_desc and valid_asc:
    if desc[0] >= asc[0]:
        print("POSSIBLE")
        print(*desc)
    else:
        print("POSSIBLE")
        print(*asc)
elif valid_desc:
    print("POSSIBLE")
    print(*desc)
elif valid_asc:
    print("POSSIBLE")
    print(*asc)
else:
    print("IMPOSSIBLE")