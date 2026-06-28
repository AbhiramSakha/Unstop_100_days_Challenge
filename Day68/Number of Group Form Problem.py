def get_anagram_groups(strs):
    n = len(strs)
    if n == 0:
        return 0

    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px = find(x)
        py = find(y)
        if px == py:
            return
        if rank[px] < rank[py]:
            parent[px] = py
        elif rank[px] > rank[py]:
            parent[py] = px
        else:
            parent[py] = px
            rank[px] += 1

    def similar(a, b):
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
                if diff > 4:
                    return False
        return diff == 0 or diff == 4

    for i in range(n):
        for j in range(i + 1, n):
            if similar(strs[i], strs[j]):
                union(i, j)

    groups = set()
    for i in range(n):
        groups.add(find(i))

    return len(groups)


if __name__ == "__main__":
    n = int(input())

    arr = []
    while len(arr) < n:
        arr.extend(input().split())

    print(get_anagram_groups(arr))