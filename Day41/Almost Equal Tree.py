import sys
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree(data):
    if not data:
        return None
    values = data.split()
    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1
    while i < len(values):
        node = queue.popleft()
        if values[i] != '-1':
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] != '-1':
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1
    return root

def is_almost_equal_tree(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.val != root2.val:
        return False

    return (
        (is_almost_equal_tree(root1.left, root2.left) and
         is_almost_equal_tree(root1.right, root2.right))
        or
        (is_almost_equal_tree(root1.left, root2.right) and
         is_almost_equal_tree(root1.right, root2.left))
    )

if __name__ == '__main__':
    line1 = sys.stdin.readline().strip()
    line2 = sys.stdin.readline().strip()
    root1 = build_tree(line1)
    root2 = build_tree(line2)
    result = is_almost_equal_tree(root1, root2)
    print('true' if result else 'false')