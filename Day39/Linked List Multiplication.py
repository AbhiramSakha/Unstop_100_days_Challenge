class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def multiply_linked_lists(l1, l2):

    # Convert linked list to number
    # (digits are stored in given traversal order)
    def to_number(head):
        num = 0

        while head:
            num = num * 10 + head.val
            head = head.next

        return num

    num1 = to_number(l1)
    num2 = to_number(l2)

    product = num1 * num2

    # Build linked list from product
    product_str = str(product)

    dummy = ListNode(0)
    curr = dummy

    for ch in product_str:
        curr.next = ListNode(int(ch))
        curr = curr.next

    return dummy.next

def build_linked_list_from_string(s):
    dummy = ListNode(0)
    current = dummy

    for char in reversed(s):
        current.next = ListNode(int(char))
        current = current.next

    return dummy.next

def linked_list_to_string(l):
    result = []

    while l:
        result.append(str(l.val))
        l = l.next

    return ''.join(result)

def main():
    import sys

    input = sys.stdin.read
    data = input().strip().split()

    n = data[0]
    m = data[1]

    l1 = build_linked_list_from_string(n)
    l2 = build_linked_list_from_string(m)

    result_head = multiply_linked_lists(l1, l2)

    result_str = linked_list_to_string(result_head)

    print(result_str)

if __name__ == "__main__":
    main()