class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def check_even_or_odd(head):
    if head is None:
        return 0

    while head.next:
        head = head.next

    return 1 if head.val % 2 == 0 else 0


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    elements = list(map(int, data[1:]))

    if n > 0:
        head = ListNode(elements[0])
        current = head
        for i in range(1, n):
            current.next = ListNode(elements[i])
            current = current.next
    else:
        head = None

    print(check_even_or_odd(head))


if __name__ == "__main__":
    main()