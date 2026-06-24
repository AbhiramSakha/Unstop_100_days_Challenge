def minimumTime(currentState, desiredState, alterablePositions):
    n = len(currentState)

    if len(desiredState) != n or len(alterablePositions) != n:
        return -1

    if any(not ('a' <= c <= 'z') for c in currentState + desiredState):
        return -1

    if any(c not in '01' for c in alterablePositions):
        return -1

    if n == 0:
        return 0

    ans = float('inf')

    for r in range(n):
        # left rotation by r positions
        rotated = currentState[r:] + currentState[:r]

        changes = 0
        possible = True

        for i in range(n):
            if rotated[i] != desiredState[i]:
                if alterablePositions[i] == '1':
                    changes += 1
                else:
                    possible = False
                    break

        if possible:
            rotation_cost = min(r, n - r) * 2
            total_cost = rotation_cost + changes * 3
            ans = min(ans, total_cost)

    return -1 if ans == float('inf') else ans


if __name__ == "__main__":
    currentState = input().strip()
    desiredState = input().strip()
    alterablePositions = input().strip()

    print(minimumTime(currentState, desiredState, alterablePositions))