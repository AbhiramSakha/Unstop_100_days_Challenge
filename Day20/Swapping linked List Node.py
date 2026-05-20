class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapNodes(head, k):
    """
    Parameters:
        head (ListNode): The head of the linked list
        k (int): The position of the nodes to be swapped
    Returns:
        ListNode: The head of the modified linked list
    """
    # Step 1: Find length of linked list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    # If kth from start and end are same, no swap needed
    if k > length or k == length - k + 1:
        return head

    # Step 2: Find kth node from start
    first = head
    for _ in range(k - 1):
        first = first.next

    # Step 3: Find kth node from end (i.e., (length - k + 1)th from start)
    second = head
    for _ in range(length - k):
        second = second.next

    # Step 4: Swap values
    first.val, second.val = second.val, first.val

    return head


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])  # Number of nodes
    values = list(map(int, data[1:n+1]))  # Node values
    k = int(data[n+1])  # Position K

    # Create linked list
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next

    head = dummy.next

    # Swap nodes
    modified_head = swapNodes(head, k)

    # Print result
    result = []
    current = modified_head
    while current:
        result.append(current.val)
        current = current.next

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()