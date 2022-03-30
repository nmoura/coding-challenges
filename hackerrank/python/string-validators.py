# https://www.hackerrank.com/challenges/string-validators


if __name__ == '__main__':
    s = input()

    alnum, alpha, digit, lower, upper = False, False, False, False, False

    for char in s:
        if not alnum:
            alnum = char.isalnum()
        if not alpha:
            alpha = char.isalpha()
        if not digit:
            digit = char.isdigit()
        if not lower:
            lower = char.islower()
        if not upper:
            upper = char.isupper()

    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
