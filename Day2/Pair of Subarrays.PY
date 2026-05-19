from collections import defaultdict
import bisect

def countEqualSumNonOverlappingPairs(arr):
    n = len(arr)
    prefix = [0] * (n + 1)

    # Compute prefix sum
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    # Map: sum -> list of (start_index, end_index)
    sum_map = defaultdict(list)

    for start in range(n):
        for end in range(start, n):
            total = prefix[end + 1] - prefix[start]
            sum_map[total].append((start, end))

    count = 0

    # For each unique sum, count non-overlapping pairs
    for subarrays in sum_map.values():
        # Sort by start index
        subarrays.sort()
        # Extract start and end positions
        starts = [s for s, e in subarrays]
        ends = [e for s, e in subarrays]

        m = len(subarrays)

        for i in range(m):
            end_i = subarrays[i][1]
            # Use binary search to find first index j where start_j > end_i
            j = bisect.bisect_right(starts, end_i)
            count += (m - j)

    return count

# --------------------------
# Reading input and printing result
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    n = data[0]
    arr = data[1:]
    print(countEqualSumNonOverlappingPairs(arr))