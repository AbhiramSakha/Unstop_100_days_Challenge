class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert_node(head, val):
    new_node = ListNode(val)
    if head[0] is None:
        head[0] = new_node
        return
    temp = head[0]
    while temp.next is not None:
        temp = temp.next
    temp.next = new_node

def print_list(node):
    if node is None:
        print("null")
        return
    while node is not None:
        print(node.val, end=" ")
        node = node.next
    print()

def delete_duplicates(head):
    """
    Delete all duplicates from a sorted linked list, keeping only distinct elements.
    """
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    current = head

    while current:
        # Skip all duplicates
        if current.next and current.val == current.next.val:
            val_to_remove = current.val
            while current and current.val == val_to_remove:
                current = current.next
            prev.next = current  # Remove duplicates
        else:
            prev = current
            current = current.next

    return dummy.next

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])  # First input is the integer N
    head = [None]  # List to hold head reference

    for i in range(1, n+1):
        temp = int(data[i])
        insert_node(head, temp)  # Insert node

    res = delete_duplicates(head[0])  # Remove duplicates
    print_list(res)  # Print the resulting linked list

if __name__ == "__main__":
    main()