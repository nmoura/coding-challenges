# https://www.hackerrank.com/challenges/30-conditional-statements


if __name__ == '__main__':
    N = int(input().strip())
    if (N % 2 > 0) or (N >= 6 and N <= 20):
        print("Weird")
    else:
        print("Not Weird")
