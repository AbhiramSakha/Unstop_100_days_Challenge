class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def user_logic(n, m, node_values, to_delete):
    if n == 0:
        return []

    # Build tree treating -1 as NULL
    if node_values[0] == -1:
        return []

    nodes = [None] * n

    for i in range(n):
        if node_values[i] != -1:
            nodes[i] = Node(node_values[i])

    for i in range(n):
        if nodes[i] is None:
            continue

        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            nodes[i].left = nodes[left]

        if right < n:
            nodes[i].right = nodes[right]

    root = nodes[0]

    delete_set = set(to_delete)
    forest = []

    def dfs(node):
        if not node:
            return None

        node.left = dfs(node.left)
        node.right = dfs(node.right)

        if node.data in delete_set:
            if node.left:
                forest.append(node.left)

            if node.right:
                forest.append(node.right)

            return None

        return node

    root = dfs(root)

    if root:
        forest.append(root)

    return forest

def main():
    import sys

    data = sys.stdin.read().strip().split()

    n = int(data[0])
    m = int(data[1])

    node_values = list(map(int, data[2:n + 2]))
    to_delete = list(map(int, data[n + 2:n + 2 + m]))

    forest_roots = user_logic(n, m, node_values, to_delete)

    def inorder(root):
        if not root:
            return []
        return inorder(root.left) + [root.data] + inorder(root.right)

    for root in forest_roots:
        print(*inorder(root))

if __name__ == "__main__":
    main()