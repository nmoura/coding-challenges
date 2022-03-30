# https://www.hackerrank.com/challenges/exceptions


n = input()

for i in range(int(n)):
    line = input()
    try:
        x, y = int(line.strip().split()[0]), int(line.strip().split()[1])
        print(x // y)
    except Exception as ex:
        print('Error Code: {}'.format(ex))
