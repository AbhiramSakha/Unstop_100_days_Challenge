class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def construct(arr, lo, hi):
    if lo > hi:
        return None
    mid = hi - ((hi - lo) // 2)
    data = arr[mid]
    left = construct(arr, lo, mid - 1)
    right = construct(arr, mid + 1, hi)
    node = Node(data, left, right)
    return node

def display(node):
    if node is None:
        return
    left = str(node.left.data) if node.left else "."
    right = str(node.right.data) if node.right else "."
    print(f"{left} <- {node.data} -> {right}")
    display(node.left)
    display(node.right)

# --- Main Execution ---
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    root = construct(arr, 0, n - 1)
    display(root)
                            