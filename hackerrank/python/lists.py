# https://www.hackerrank.com/challenges/python-lists


if __name__ == '__main__':
    N = int(input())

    ints = []
    exec_cmd = {'insert': ints.insert, 'append': ints.append,
                'remove': ints.remove, 'sort': ints.sort,
                'pop': ints.pop, 'reverse': ints.reverse}

    for index in range(N):
        cmdLine = input()
        command = cmdLine.split(' ')[0]
        args = [int(n) for n in cmdLine.split(' ')[1:]]

        if command == "print":
            print(ints)
            continue
        exec_cmd[command](*args)
