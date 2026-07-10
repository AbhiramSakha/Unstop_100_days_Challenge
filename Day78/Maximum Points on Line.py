from math import gcd
from collections import defaultdict

def user_logic(points):
    """
    Write your logic here.
    Parameters:
        points (list): List of tuples where each tuple contains two integers (x, y)
    Returns:
        int: Maximum number of points that lie on a line
    """
    n = len(points)
    if n <= 2:
        return n

    ans = 2

    for i in range(n):
        slopes = defaultdict(int)

        for j in range(i + 1, n):
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]

            g = gcd(dx, dy)
            dx //= g
            dy //= g

            # Normalize the direction
            if dx < 0:
                dx = -dx
                dy = -dy
            elif dx == 0:
                dy = 1
            elif dy == 0:
                dx = 1

            slopes[(dx, dy)] += 1
            ans = max(ans, slopes[(dx, dy)] + 1)

    return ans


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    points = []

    idx = 1
    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx + 1])
        points.append((x, y))
        idx += 2

    print(user_logic(points))


if __name__ == "__main__":
    main()