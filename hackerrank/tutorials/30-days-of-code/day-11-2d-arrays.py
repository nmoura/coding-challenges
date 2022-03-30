# https://www.hackerrank.com/challenges/30-2d-arrays


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for y in range(len(arr) - 2):
        for x in range(len(arr[y]) -2):
            hg_line_1 = arr[y][x] + arr[y][x + 1] + arr[y][x + 2]
            hg_line_2 = arr[y + 1][x + 1]
            hg_line_3 = arr[y + 2][x] + arr[y + 2][x + 1] + arr[y + 2][x + 2]
            hourglass_sum = hg_line_1 + hg_line_2 + hg_line_3
            if 'hourglass_max_sum' not in globals() or hourglass_sum > hourglass_max_sum:
                hourglass_max_sum = hourglass_sum

    print(hourglass_max_sum)
