def find_digit_at_position(N):
    length = 1
    count = 9
    start = 1

    while N > length * count:
        N -= length * count
        length += 1
        count *= 10
        start *= 10

    number = start + (N - 1) // length
    digit_index = (N - 1) % length

    return str(number)[digit_index]

def main():
    import sys
    input = sys.stdin.read
    data = input().strip()

    N = int(data)

    result = find_digit_at_position(N)
    print(result)

if __name__ == "__main__":
    main()