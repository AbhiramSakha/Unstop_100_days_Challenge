MOD = 10**9 + 7

def homogenous_substring(s):
    ans = 0
    count = 1

    for i in range(len(s)):
        if i > 0 and s[i] == s[i - 1]:
            count += 1
        else:
            count = 1

        ans = (ans + count) % MOD

    return ans


def main():
    import sys
    input = sys.stdin.read
    s = input().strip()

    result = homogenous_substring(s)
    print(result)

if __name__ == "__main__":
    main()