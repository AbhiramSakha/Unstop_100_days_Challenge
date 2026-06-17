class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def user_logic(head, k):
    dummy = Node(0)
    tail = dummy

    curr = head

    while curr:
        temp = curr
        cnt = 0
        total = 0

        while temp and cnt < k:
            total += temp.data
            temp = temp.next
            cnt += 1

        if cnt < k:
            while curr:
                tail.next = Node(curr.data)
                tail = tail.next
                curr = curr.next
            break

        mean = total // k

        if mean % 2 == 0:
            tail.next = Node(mean)
            tail = tail.next

        for _ in range(k):
            curr = curr.next

    return dummy.next

def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=" --> ")
        current = current.next
    print("null")

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    k = int(data[0])
    n = int(data[1])
    
    head = None
    tail = None
    
    index = 2
    for _ in range(n):
        data_value = int(data[index])
        new_node = Node(data_value)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
        index += 1
    
    # Call user logic function
    modified_head = user_logic(head, k)
    
    # Print the resulting linked list
    print_list(modified_head)

if __name__ == "__main__":
    main()