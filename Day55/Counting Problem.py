from collections import Counter
import heapq

def count_unique_numbers(arr):
    freq = Counter(arr)

    max_heap = [-x for x in freq]
    heapq.heapify(max_heap)

    unique_count = 0

    while max_heap:
        x = -heapq.heappop(max_heap)

        if x not in freq:
            continue

        cnt = freq.pop(x)

        if cnt == 1:
            unique_count += 1

            half = x // 2
            if half > 0:
                if half in freq:
                    freq[half] += 1
                else:
                    freq[half] = 1
                    heapq.heappush(max_heap, -half)

    return unique_count


def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))

    n = data[0]
    arr = data[1:1 + n]

    print(count_unique_numbers(arr))

if __name__ == "__main__":
    main()