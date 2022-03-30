# https://www.hackerrank.com/challenges/python-string-formatting


def print_formatted(number):
    length = len(bin(number).replace('0b', ''))
    for i in range(1, number + 1):
        deci = str(i).rjust(length)
        octa = str(oct(i).replace('0o', '')).rjust(length)
        hexa = str(hex(i).replace('0x', '')).upper().rjust(length)
        bina = str(bin(i).replace('0b', '')).rjust(length)
        print("{} {} {} {}".format(deci, octa, hexa, bina))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
