def count_workers_unable_to_collect_parts(workers, parts):
    """
    Write your logic here.
    Parameters:
        workers (list): List of integers representing the type of part each worker can handle
        parts (list): List of integers representing the type of part at each position on the conveyor belt
    Returns:
        int: Number of workers who are unable to collect a part
    """
    count = [0, 0]
    for w in workers:
        count[w] += 1

    for i, p in enumerate(parts):
        if count[p] == 0:
            return len(parts) - i
        count[p] -= 1

    return 0


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    workers = list(map(int, data[1:n+1]))
    parts = list(map(int, data[n+1:2*n+1]))

    result = count_workers_unable_to_collect_parts(workers, parts)
    print(result)

if __name__ == "__main__":
    main()