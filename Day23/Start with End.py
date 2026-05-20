
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def build_linked_list(size, elements):
    if size == 0:
        return None
    head = Node(elements[0])
    tail = head
    for i in range(1, size):
        tail.next = Node(elements[i])
        tail = tail.next
    return head

def pair_sum(head):
    """
    Write your logic here.
    Parameters:
        head (Node): Head of the linked list
    Returns:
        int: Maximum sum of symmetric pairs
    """
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    elements = list(map(int, data[1:n+1]))  # Next n inputs are the elements of the linked list
    
    head = build_linked_list(n, elements)
    
    # Call the user logic function and print the output
    result = pair_sum(head)
    print(result)

if __name__ == "__main__":
    main()
