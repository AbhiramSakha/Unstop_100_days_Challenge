class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_sweetness(n, sweetness, tree_structure):
    import sys
    sys.setrecursionlimit(10**6)

    NEG = -10**18

    def dfs(u):
        if u == -1:
            return 0, NEG

        l, r = tree_structure[u - 1]

        left_down, left_best = dfs(l)
        right_down, right_best = dfs(r)

        down = sweetness[u - 1] + max(0, left_down, right_down)
        through = sweetness[u - 1] + max(0, left_down) + max(0, right_down)

        best = max(left_best, right_best, through)

        return down, best

    return max(0, dfs(1)[1])


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    idx = 0
    n = int(data[idx])
    idx += 1

    sweetness = []
    for _ in range(n):
        sweetness.append(int(data[idx]))
        idx += 1

    tree_structure = []
    for _ in range(n):
        l = int(data[idx])
        r = int(data[idx + 1])
        tree_structure.append((l, r))
        idx += 2

    print(max_sweetness(n, sweetness, tree_structure))

if __name__ == "__main__":
    main()