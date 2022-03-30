# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    for idx in range(1, len(arr)):
        if arr[idx] < arr[idx - 1]:
            print(arr[idx])
            break
