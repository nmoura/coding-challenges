# https://www.hackerrank.com/challenges/nested-list


if __name__ == '__main__':
    names_scores_lists = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names_scores_lists.append([name, score])

    scores_names = {}
    for nsl in names_scores_lists:
        try:
            scores_names[nsl[1]].append(nsl[0])
        except KeyError:
            scores_names[nsl[1]] = [nsl[0]]

    scores_names.pop(min(scores_names))

    for name in sorted(scores_names[min(scores_names)]):
        print(name)
