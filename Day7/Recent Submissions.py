# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

def max_submission_queue_size(n, arr):
    queue = deque()
    max_size = 0

    for t in arr:
        # Remove submissions that are <= t - 5000
        while queue and queue[0] <= t - 5000:
            queue.popleft()
        queue.append(t)
        max_size = max(max_size, len(queue))

    return max_size

# Sample Input Reading
n = int(input())
arr = list(map(int, input().split()))
print(max_submission_queue_size(n, arr))