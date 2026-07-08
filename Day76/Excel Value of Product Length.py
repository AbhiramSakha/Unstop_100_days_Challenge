def to_excel(num):
    res = []
    while num > 0:
        num -= 1
        res.append(chr(ord('A') + (num % 26)))
        num //= 26
    return "".join(reversed(res))


def user_logic(words):
    n = len(words)

    masks = []
    lengths = []

    for w in words:
        mask = 0
        for ch in set(w):
            mask |= 1 << (ord(ch) - ord('a'))
        masks.append(mask)
        lengths.append(len(w))

    max_product = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (masks[i] & masks[j]) == 0:
                prod = lengths[i] * lengths[j]
                if prod > max_product:
                    max_product = prod

    if max_product == 0:
        return "0"

    return to_excel(max_product)


def main():
    import sys
    input = sys.stdin.read

    data = input().split()
    n = int(data[0])
    words = data[1:]

    print(user_logic(words))


if __name__ == "__main__":
    main()