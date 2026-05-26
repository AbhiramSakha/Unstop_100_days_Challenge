def check_word_break(goal, target_words):
    word_set = set(target_words)
    n = len(goal)

    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and goal[j:i] in word_set:
                dp[i] = True
                break

    return 1 if dp[n] else 0

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    goal = data[1]
    target_words = data[2:2+n]

    result = check_word_break(goal, target_words)
    print(result)

if __name__ == "__main__":
    main()