def solution(cap, n, deliveries, pickups):
    answer = 0
    
    while deliveries and pickups and deliveries[-1] == 0 and pickups[-1] == 0:
        n -= 1
        deliveries.pop()
        pickups.pop()

    while deliveries or pickups:
        if deliveries:
            deliveries[-1] -= cap
            while deliveries[-1] <= 0:
                temp = deliveries.pop()
                if deliveries:
                    deliveries[-1] += temp
                else:
                    break
        
        if pickups:
            pickups[-1] -= cap
            while pickups[-1] <= 0:
                temp = pickups.pop()
                if pickups:
                    pickups[-1] += temp
                else:
                    break
        
        answer += 2 * n
        n = max(len(deliveries), len(pickups))
        
    return answer