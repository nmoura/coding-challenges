# https://www.hackerrank.com/challenges/itertools-product
from itertools import product


def get_input():
    return list(map(int, input().split()))


for i in product(get_input(), get_input()):
    print(i, end=' ')
