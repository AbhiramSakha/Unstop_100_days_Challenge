def main():
    import sys
    input = sys.stdin.read
    N = int(input().strip())

    # Compute the largest power of 2 less than or equal to N
    result = 1 << (N.bit_length() - 1)
    print(result)

if __name__ == "__main__":
    main()