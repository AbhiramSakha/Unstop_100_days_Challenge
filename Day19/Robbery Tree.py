class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def insertLevelOrder(arr, i):
    # Base case
    if i >= len(arr) or arr[i] == "null":
        return None

    root = TreeNode(int(arr[i]))
    root.left = insertLevelOrder(arr, 2 * i + 1)
    root.right = insertLevelOrder(arr, 2 * i + 2)

    return root


def user_logic(root):
    def dfs(node):
        if not node:
            return (0, 0)  # (rob_this, skip_this)

        left_rob, left_skip = dfs(node.left)
        right_rob, right_skip = dfs(node.right)

        # Rob current node
        rob_this = node.val + left_skip + right_skip

        # Skip current node
        skip_this = max(left_rob, left_skip) + max(right_rob, right_skip)

        return (rob_this, skip_this)

    return max(dfs(root))


def main():
    import sys
    data = sys.stdin.read().strip().split()

    # Build the tree from the input level-order traversal
    root = insertLevelOrder(data, 0)

    # Compute and print result
    result = user_logic(root)
    print(result)


if __name__ == "__main__":
    main()