# https://www.hackerrank.com/challenges/30-review-loop


for _ in range(int(input())):
    S = input()
    print("{} {}".format(S[::2], S[1::2]))
