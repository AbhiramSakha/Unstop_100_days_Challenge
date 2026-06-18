def count_xor_setbit_triplets(N):
    pop = [0] * (N + 1)
    for i in range(1, N + 1):
        pop[i] = pop[i >> 1] + (i & 1)

    count = 0

    for a in range(1, N + 1):
        for b in range(a + 1, N + 1):
            c = a ^ b

            if c <= b or c > N:
                continue

            if pop[a] == pop[b] == pop[c]:
                count += 1

    return count


def main():
    import sys

    N = int(sys.stdin.read().strip())
    print(count_xor_setbit_triplets(N))


if __name__ == "__main__":
    main()