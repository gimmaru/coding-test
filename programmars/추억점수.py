from collections import defaultdict


def solution(name, yearning, photo):
    answer = []

    name2yearning = defaultdict(int)
    for n, y in zip(name, yearning):
        name2yearning[n] = y

    for people in photo:
        score = 0
        for name in people:
            score += name2yearning[name]
        answer += score,

    return answer