# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque
import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def buildTree(arr):
    if not arr or arr[0] == "N":
        return None

    root = Node(int(arr[0]))
    q = deque([root])

    i = 1

    while q and i < len(arr):
        curr = q.popleft()

        if i < len(arr) and arr[i] != "N":
            curr.left = Node(int(arr[i]))
            q.append(curr.left)
        i += 1

        if i < len(arr) and arr[i] != "N":
            curr.right = Node(int(arr[i]))
            q.append(curr.right)
        i += 1

    return root


def lowestCommonAncestor(root, p, q):
    if root is None:
        return None

    if root.val == p or root.val == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


def main():
    input = sys.stdin.readline

    n = int(input().strip())

    arr = input().split()

    p, q = map(int, input().split())

    root = buildTree(arr)

    lca = lowestCommonAncestor(root, p, q)

    print(lca.val)


if __name__ == "__main__":
    main()
                            