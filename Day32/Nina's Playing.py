from collections import defaultdict, deque

# Placeholder function where the user will write their logic

def can_divide_into_groups(n, cards):
    graph = defaultdict(list)
    degree = [0] * (n + 1)

    for a, b in cards:
        if a == b:
            return "NO"

        graph[a].append(b)
        graph[b].append(a)

        degree[a] += 1
        degree[b] += 1

    # Every number must appear exactly twice
    for i in range(1, n + 1):
        if degree[i] != 2:
            return "NO"

    visited = [False] * (n + 1)

    # Graph must contain only even cycles
    for i in range(1, n + 1):
        if not visited[i]:
            q = deque([(i, 0)])
            visited[i] = True
            count = 0

            while q:
                node, dist = q.popleft()
                count += 1

                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append((nei, dist + 1))

            if count % 2 == 1:
                return "NO"

    return "YES"


# Main function to handle input and output

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    index = 0
    t = int(data[index])
    index += 1

    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1

        cards = []
        for _ in range(n):
            a = int(data[index])
            b = int(data[index + 1])
            cards.append((a, b))
            index += 2

        # Call user logic function and store the result
        result = can_divide_into_groups(n, cards)
        results.append(result)

    # Print all the results for each test case
    for result in results:
        print(result)

if __name__ == "__main__":
    main()