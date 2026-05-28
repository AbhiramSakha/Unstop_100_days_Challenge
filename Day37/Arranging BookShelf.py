class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def user_logic(l1, l2):
    """
    Write your logic here.
    Parameters:
        l1 (Node): Head of the first linked list
        l2 (Node): Head of the second linked list
    Returns:
        Node: Head of the merged linked list in sorted order
    """

    dummy = Node(-1)

    tail = dummy

    while l1 and l2:

        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    if l1:
        tail.next = l1

    if l2:
        tail.next = l2

    return dummy.next

def print_list(head):

    while head:
        print(head.val, end=" ")
        head = head.next

    print()

def main():
    import sys

    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    m = int(data[1])

    l1 = None
    l2 = None

    tail = None

    index = 2

    # First linked list
    for i in range(n):

        val = int(data[index])

        new_node = Node(val)

        if l1 is None:
            l1 = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

        index += 1

    tail = None

    for i in range(m):

        val = int(data[index])

        new_node = Node(val)

        if l2 is None:
            l2 = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

        index += 1

    merged_list = user_logic(l1, l2)

    print_list(merged_list)

if __name__ == "__main__":
    main()