def erase_overlap_intervals(intervals):
    # Sort by end time
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    end = float('-inf')

    for interval in intervals:
        if interval[0] >= end:
            # No overlap, accept it
            end = interval[1]
        else:
            # Overlap, remove this interval
            count += 1
    
    return count

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])  # M is unused in the problem (can be ignored safely)
    
    intervals = []
    index = 2
    for _ in range(N):
        intervals.append([int(data[index]), int(data[index + 1])])
        index += 2
    
    result = erase_overlap_intervals(intervals)
    print(result)
                            