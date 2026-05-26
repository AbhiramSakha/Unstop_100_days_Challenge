def determine_winner(n, smit_str, joy_str):
    if n == 0:
        return "TIE"

    unique_smit = len(set(smit_str))
    unique_joy = len(set(joy_str))

    mean_smit = unique_smit / n
    mean_joy = unique_joy / n

    if mean_smit > mean_joy:
        return "SMIT"
    elif mean_joy > mean_smit:
        return "JOY"
    else:
        return "TIE"

# Input Reading
n = int(input())
smit_str = input().strip()
joy_str = input().strip()

# Output Result
print(determine_winner(n, smit_str, joy_str))
                            