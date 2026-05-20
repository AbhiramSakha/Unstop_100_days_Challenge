class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def make_tree(idx, n, arr):
    if idx >= n or arr[idx] == -1:
        return None
    root = TreeNode(arr[idx])
    root.left = make_tree(2 * idx + 1, n, arr)
    root.right = make_tree(2 * idx + 2, n, arr)
    return root

def user_logic(root):
    def dfs(node, current):
        if not node:
            return 0

        # Build the binary number
        current = (current << 1) | node.val

        # If leaf node, return the number formed
        if not node.left and not node.right:
            return current

        # Otherwise, continue DFS
        return dfs(node.left, current) + dfs(node.right, current)

    return dfs(root, 0)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))
    root = make_tree(0, n, arr)
    result = user_logic(root)
    print(result)

if __name__ == "__main__":
    main()