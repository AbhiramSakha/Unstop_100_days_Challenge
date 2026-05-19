def process(string):
    stack = []
    for char in string:
        if char == '#':
            if stack:
                stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

def userLogic(bob, alice):
    return process(bob) == process(alice)

if __name__ == "__main__":
    bob = input()
    alice = input()
    result = userLogic(bob, alice)
    print("YES" if result else "NO")