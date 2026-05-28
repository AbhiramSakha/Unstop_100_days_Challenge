class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_mean_list(head, k, n):
    """
    Write your logic here.
    Parameters:
        head (Node): Head of the linked list.
        k (int): Number of nodes for which you will calculate mean.
        n (int): Size of linked list.
    Returns:
        Node: Head of the newly created linked list.
    """

    new_head = None
    new_tail = None

    curr = head

    while curr:

        temp = []

        total = 0
        count = 0

        while curr and count < k:

            temp.append(curr.data)

            total += curr.data

            curr = curr.next

            count += 1

        # Remaining nodes are less than k
        if count < k:

            for val in temp:

                node = Node(val)

                if new_head is None:
                    new_head = node
                    new_tail = node
                else:
                    new_tail.next = node
                    new_tail = node

            break

        mean = total // k

        if mean % 2 == 0:

            node = Node(mean)

            if new_head is None:
                new_head = node
                new_tail = node
            else:
                new_tail.next = node
                new_tail = node

    return new_head

def print_list(head):
    curr = head

    while curr:
        print(curr.data, end=" --> ")
        curr = curr.next

    print("null")

def main():
    import sys

    input = sys.stdin.read
    data = input().strip().split()

    k = int(data[0])
    n = int(data[1])

    elements = list(map(int, data[2:]))

    head = None
    tail = None

    for data in elements:

        new_node = Node(data)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    mean_list_head = get_mean_list(head, k, n)

    print_list(mean_list_head)

if __name__ == "__main__":
    main()