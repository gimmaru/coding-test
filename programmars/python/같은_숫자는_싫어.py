def solution(arr):
    answer = [-1]
    for num in arr:
        if answer[-1] != num:
            answer += num,
    return answer[1:]

def solution(arr):
    prev, answer = -1, []
    for num in arr:
        if prev != num:
            prev = num
            answer += num,
    return answer