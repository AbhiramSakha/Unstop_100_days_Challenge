def count_mismatched_indices(heights):
    expected = sorted(heights)
    count = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    heights = list(map(int, input().split()))
    print(count_mismatched_indices(heights))