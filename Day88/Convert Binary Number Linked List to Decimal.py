class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def binary_to_decimal(head):
    result = 0
    while head:
        result = (result << 1) | head.data
        head = head.next
    return result


def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n = data[0]
    values = data[1:]

    head = Node(values[0])
    curr = head
    for i in range(1, n):
        curr.next = Node(values[i])
        curr = curr.next

    print(binary_to_decimal(head))


if __name__ == "__main__":
    main()