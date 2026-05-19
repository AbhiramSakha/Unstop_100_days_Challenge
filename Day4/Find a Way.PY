import sys
sys.setrecursionlimit(10**7)  # To handle deep trees

class TreeNode:
    __slots__ = ('left', 'right')  # Memory efficient
    def __init__(self):
        self.left = None
        self.right = None

def user_logic(root):
    """
    Finds the maximum length of the marathon, which is the diameter of the binary tree.
    """
    max_diameter = [0]

    def dfs(node):
        if not node:
            return 0
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)
        max_diameter[0] = max(max_diameter[0], left_depth + right_depth)
        return 1 + max(left_depth, right_depth)

    dfs(root)
    return max_diameter[0]

def main():
    input = sys.stdin.read().split()
    n = int(input[0])
    
    nodes = [(int(input[i]), int(input[i+1])) for i in range(1, len(input), 2)]

    if n == 0:
        print(0)
        return

    # Step 1: Create tree nodes
    tree_nodes = [TreeNode() for _ in range(n)]

    # Step 2: Assign children
    for i, (l, r) in enumerate(nodes):
        if l != -1:
            tree_nodes[i].left = tree_nodes[l - 1]
        if r != -1:
            tree_nodes[i].right = tree_nodes[r - 1]

    # Step 3: Root is at index 0
    root = tree_nodes[0]
    
    # Step 4: Compute the result
    result = user_logic(root)
    print(result)

if __name__ == "__main__":
    main()