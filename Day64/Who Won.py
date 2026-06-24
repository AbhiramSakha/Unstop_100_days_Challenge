def determine_winner(d, k):
    left, right = 0, d // k

    while left <= right:
        mid = (left + right) // 2
        if 2 * (mid * k) * (mid * k) <= d * d:
            left = mid + 1
        else:
            right = mid - 1

    t = right

    if ((t + 1) ** 2 + t ** 2) * k * k <= d * d:
        return "Ashish"
    else:
        return "Utkarsh"

def main():
    import sys
    data = sys.stdin.read().strip().split()

    d = int(data[0])
    k = int(data[1])

    print(determine_winner(d, k))

if __name__ == "__main__":
    main()