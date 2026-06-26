import heapq

def process_queries(queries):
    lower = []  # max heap (store negatives)
    upper = []  # min heap
    result = []

    for typ, val in queries:
        if typ == "add":
            val = int(val)

            if not lower or val <= -lower[0]:
                heapq.heappush(lower, -val)
            else:
                heapq.heappush(upper, val)

            if len(lower) > len(upper) + 1:
                heapq.heappush(upper, -heapq.heappop(lower))
            elif len(upper) > len(lower):
                heapq.heappush(lower, -heapq.heappop(upper))

        else:  # get
            if len(lower) > len(upper):
                result.append(float(-lower[0]))
            else:
                result.append(((-lower[0]) + upper[0]) / 2.0)

    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    k = int(data[0])
    queries = []

    for i in range(1, k + 1):
        line = data[i].split()
        if line[0] == "add":
            queries.append(("add", float(line[1])))
        else:
            queries.append(("get", None))

    results = process_queries(queries)

    for x in results:
        print(f"{x:.1f}")

if __name__ == "__main__":
    main()