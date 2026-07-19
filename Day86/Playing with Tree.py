class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def lowest_common_ancestor(root, p, q):
    while root:
        if p < root.data and q < root.data:
            root = root.left
        elif p > root.data and q > root.data:
            root = root.right
        else:
            return root.data
    return -1


def main():
    import sys

    data = list(map(int, sys.stdin.read().split()))

    n = data[0]
    nodes = data[1:n + 1]
    x = data[n + 1]
    y = data[n + 2]

    root = None
    for node in nodes:
        root = insert(root, node)

    print(lowest_common_ancestor(root, x, y))


if __name__ == "__main__":
    main()