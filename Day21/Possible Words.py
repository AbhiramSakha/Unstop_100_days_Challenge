def letterCombinations(digits):
    # If input is empty, return empty list
    if not digits:
        return []

    # Mapping of digits to letters
    phone = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    result = []

    def backtrack(index, current):
        # If current combination is complete
        if index == len(digits):
            result.append(current)
            return

        # Try all letters for the current digit
        for ch in phone[digits[index]]:
            backtrack(index + 1, current + ch)

    backtrack(0, "")
    return result


if __name__ == '__main__':
    digits = input().strip()
    result = letterCombinations(digits)
    result.sort()
    print(' '.join(result))