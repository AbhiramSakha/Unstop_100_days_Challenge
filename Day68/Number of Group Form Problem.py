def get_anagram_groups(strs):
    n = len(strs)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[py] = px

    def similar(a, b):
        diff = 0
        for x, y in zip(a, b):
            if x != y:
                diff += 1
                if diff > 4:
                    return False
        return diff == 0 or diff == 4

    for i in range(n):
        for j in range(i + 1, n):
            if similar(strs[i], strs[j]):
                union(i, j)

    return len({find(i) for i in range(n)})

if __name__ == "__main__":
    n = int(input())
    arr = input().split()
    print(get_anagram_groups(arr))