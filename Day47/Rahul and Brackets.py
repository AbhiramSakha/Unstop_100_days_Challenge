def user_logic(s):
    balance = 0
    moves = 0

    for ch in s:
        if ch == '(':
            balance += 1
        else:
            if balance > 0:
                balance -= 1
            else:
                moves += 1

    moves += balance  

    M = moves

    if M < 2:
        return 0

    is_prime = [True] * (M + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= M:
        if is_prime[p]:
            for multiple in range(p * p, M + 1, p):
                is_prime[multiple] = False
        p += 1

    return sum(is_prime)


def main():
    import sys
    input = sys.stdin.read
    s = input().strip()

    result = user_logic(s)
    print(result)

if __name__ == "__main__":
    main()