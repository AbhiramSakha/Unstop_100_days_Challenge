def user_logic(intervals):
    """
    Write your logic here.
    Parameters:
        intervals (list): List of intervals where each interval is a list of two integers [start, end]
    Returns:
        int: Minimum length among the merged intervals
    """
    intervals.sort()

    merged = []
    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    ans = float('inf')
    for start, end in merged:
        ans = min(ans, end - start)

    return ans


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    intervals = []
    idx = 1

    for _ in range(n):
        start = int(data[idx])
        end = int(data[idx + 1])
        intervals.append([start, end])
        idx += 2

    print(user_logic(intervals))


if __name__ == "__main__":
    main()