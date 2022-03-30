# https://www.hackerrank.com/challenges/python-mutations


def mutate_string(string, position, character):
    listString = list(string)
    listString[position] = character
    return ''.join(listString)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
