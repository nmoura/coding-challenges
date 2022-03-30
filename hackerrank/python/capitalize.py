# https://www.hackerrank.com/challenges/capitalize


def solve(s):
    return(' '.join(uniqName.capitalize() for uniqName in s.split(' ')))


if __name__ == '__main__':
    s = input()
    print(solve(s))
