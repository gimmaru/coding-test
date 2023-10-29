def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    
    prev_e = 0
    for s, e in targets:
        if s >= prev_e:
            prev_e = e
            answer += 1
    
    return answer