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

def count_palindromic_paths(root):
    """
    Write your logic here.
    Parameters:
        root (TreeNode): The root of the binary tree
    Returns:
        int: Number of palindromic paths from root to leaf nodes
    """
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    arr = list(map(int, data[1:]))  # Remaining input is the level order array of the binary tree
    
    root = make_tree(0, n, arr)
    
    # Call user logic function and print the output
    result = count_palindromic_paths(root)
    print(result)

if __name__ == "__main__":
    main()