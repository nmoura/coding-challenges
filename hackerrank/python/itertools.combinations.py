# https://www.hackerrank.com/challenges/itertools-combinations
from itertools import combinations


s, k = input().split()
s = sorted(s)
k = int(k)


for size in range(1, k + 1):
    for comb in sorted(combinations(s, size)):
        print(''.join(comb))
