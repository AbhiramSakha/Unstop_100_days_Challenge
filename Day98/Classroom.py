def user_logic(n, seat_preferences):
    """
    Returns the final seating arrangement where
    result[i] = seat occupied by student (i+1)
    """

    occupied = [False] * (n + 1)
    result = [0] * n

    for student in range(n):
        seat = seat_preferences[student]

        while occupied[seat]:
            seat += 1
            if seat > n:
                seat = 1

        occupied[seat] = True
        result[student] = seat

    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    seat_preferences = list(map(int, data[1:]))

    final_seating = user_logic(n, seat_preferences)

    print(" ".join(map(str, final_seating)))


if __name__ == "__main__":
    main()