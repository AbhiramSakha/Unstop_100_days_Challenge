class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def user_logic(bst1_nodes, bst2_nodes):
    """
    Parameters:
        bst1_nodes (list): List of integers representing the node values of BST1
        bst2_nodes (list): List of integers representing the node values of BST2
    Returns:
        list: All node values from both BSTs in sorted order
    """
    # Combine both BST node values
    merged = bst1_nodes + bst2_nodes

    # Sort the combined list
    merged.sort()

    return merged


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    N = int(data[0])  # Number of nodes in the first BST
    bst1_nodes = list(map(int, data[1:N+1]))  # Node values of bst1
    
    M = int(data[N+1])  # Number of nodes in the second BST
    bst2_nodes = list(map(int, data[N+2:N+2+M]))  # Node values of bst2
    
    # Call user logic function and get the result
    result = user_logic(bst1_nodes, bst2_nodes)
    
    # Print the output as space-separated integers
    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()