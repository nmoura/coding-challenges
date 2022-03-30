# https://www.hackerrank.com/challenges/30-binary-numbers


if __name__ == '__main__':
    n = int(input())

    binaryList = []

    while n > 0:
        binaryList.append(n % 2)
        n = n // 2

    binaryList.reverse()

    max_ones = 0
    count = 0

    for number in binaryList:
        if number == 1:
            count += 1
        else:
            count = 0
        if count > max_ones:
            max_ones = count

    print(max_ones)
