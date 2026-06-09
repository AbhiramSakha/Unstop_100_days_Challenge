def user_logic(arr):
    n = len(arr)

    total_md = 0
    best_reduction = 0

    for i in range(1, n):
        diff = abs(arr[i] - arr[i - 1])
        sq = diff * diff

        total_md += sq
        best_reduction = max(best_reduction, sq // 2)

    return total_md - best_reduction


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    N = int(data[0])
    arr = list(map(int, data[1:]))

    result = user_logic(arr)
    print(result)

if __name__ == "__main__":
    main()