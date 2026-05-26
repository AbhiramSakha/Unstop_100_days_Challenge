class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def remove_last_occurrences(head):
    """
    Write your logic here to remove the last occurrence of all elements in the linked list.
    
    Parameters:
        head (ListNode): The head of the linked list.
    Returns:
        ListNode: The head of the modified linked list.
    """
    pass

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    values = list(map(int, data[1:]))  # Remaining input is the list of integers
    
    if n == 0:
        print("")
        return
    
    # Create linked list from input values
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    
    # Call user logic function
    modified_head = remove_last_occurrences(head)
    
    # Print the modified linked list
    print_linked_list(modified_head)

if __name__ == "__main__":
    main()