# https://www.hackerrank.com/challenges/no-idea


def get_happiness(array, a, b):
    return sum((i in a) - (i in b) for i in array)

    
if __name__ == '__main__':
    nm = input()
    array = [ int(i) for i in input().split() ]
    a = set([ int(i) for i in input().split()])
    b = set([ int(i) for i in input().split()])
    print(get_happiness(array, a, b))
