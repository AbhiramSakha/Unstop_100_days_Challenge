from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def user_logic(traversal):
    stack = []
    i = 0
    n = len(traversal)

    while i < n:
        depth = 0

        while i < n and traversal[i] == '-':
            depth += 1
            i += 1

        value = 0
        while i < n and traversal[i].isdigit():
            value = value * 10 + int(traversal[i])
            i += 1

        node = TreeNode(value)

        while len(stack) > depth:
            stack.pop()

        if stack:
            parent = stack[-1]

            if parent.left is None:
                parent.left = node
            else:
                parent.right = node

        stack.append(node)

    root = stack[0]

    result = []
    q = deque([root])

    while q:
        node = q.popleft()

        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)

    return result

def main():
    import sys
    input = sys.stdin.read
    traversal = input().strip()
    
    result = user_logic(traversal)
    
    print("[", end="")
    for i in range(len(result)):
        if result[i] is None:
            print("null", end="")
        else:
            print(result[i], end="")
        if i != len(result) - 1:
            print(", ", end="")
    print("]")

if __name__ == "__main__":
    main()