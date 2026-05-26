class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val <= root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def sum_of_values_in_range(root, start, end):
    if not root:
        return 0

    if root.val < start:
        # Current value is too small, only check right subtree
        return sum_of_values_in_range(root.right, start, end)
    elif root.val > end:
        # Current value is too big, only check left subtree
        return sum_of_values_in_range(root.left, start, end)
    else:
        # Current value is in range, include it and explore both sides
        return (root.val +
                sum_of_values_in_range(root.left, start, end) +
                sum_of_values_in_range(root.right, start, end))

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    values = list(map(int, data[1:n+1]))
    start, end = int(data[n+1]), int(data[n+2])

    root = None
    for val in values:
        root = insert_into_bst(root, val)

    result = sum_of_values_in_range(root, start, end)
    print(result)

if __name__ == "__main__":
    main()
                            