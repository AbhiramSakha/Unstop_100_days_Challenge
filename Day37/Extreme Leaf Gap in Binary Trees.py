from collections import deque
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])

    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        if i < len(arr):
            node.left = TreeNode(arr[i])
            queue.append(node.left)
            i += 1

        if i < len(arr):
            node.right = TreeNode(arr[i])
            queue.append(node.right)
            i += 1

    return root


def maximum_abs_diff(root):

    min_leaf = float('inf')
    max_leaf = float('-inf')

    def dfs(node):
        nonlocal min_leaf, max_leaf

        if not node:
            return

        # Leaf node
        if node.left is None and node.right is None:
            min_leaf = min(min_leaf, node.val)
            max_leaf = max(max_leaf, node.val)
            return

        dfs(node.left)
        dfs(node.right)

    dfs(root)

    # If only one leaf exists
    if min_leaf == float('inf'):
        return 0

    return abs(max_leaf - min_leaf)


def main():

    data = sys.stdin.read().strip().split()

    if not data:
        return

    idx = 0

    t = int(data[idx])
    idx += 1

    results = []

    for _ in range(t):

        level = int(data[idx])
        idx += 1

        total_nodes = (2 ** level) - 1

        arr = list(map(int, data[idx:idx + total_nodes]))
        idx += total_nodes

        root = create_tree(arr)

        results.append(maximum_abs_diff(root))

    print("\n".join(map(str, results)))


if __name__ == "__main__":
    main()