def user_logic(n, s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    ans = []
    i = 0

    while i < n:
        if s[i] not in vowels:
            ans.append(s[i])
            i += 1
        else:
            j = i
            while j < n and s[j] in vowels:
                j += 1

            ans.append(s[i:j])

            if j - i == 2:
                ans.append('$')

            i = j

    return "".join(ans)


def main():
    n = int(input())
    s = input().strip()
    print(user_logic(n, s))


if __name__ == "__main__":
    main()