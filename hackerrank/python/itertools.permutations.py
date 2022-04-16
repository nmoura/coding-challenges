https://www.hackerrank.com/challenges/itertools-permutations
from itertools import permutations


s, k = input().split()
for i in sorted(permutations(s, int(k))):
   print(''.join(i))
