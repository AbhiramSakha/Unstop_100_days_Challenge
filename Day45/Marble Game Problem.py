import heapq

def play_game(marbles):
    if len(marbles) == 1:
        return marbles[0]

    heap = [-x for x in marbles]
    heapq.heapify(heap)

    while len(heap) > 1:
        first = -heapq.heappop(heap)
        second = -heapq.heappop(heap)

        total = first + second

        if total % 2 == 0:
            heapq.heappush(heap, -(total // 2))
        # else both selected persons disappear

    return -heap[0] if heap else 0


def main():
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    marbles = list(map(int, data[1:n + 1]))

    print(play_game(marbles))

if __name__ == "__main__":
    main()