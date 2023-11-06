def solution(park, routes):
    H, W = len(park), len(park[0])
    get_start_index = False
    
    for i, road in enumerate(park):
        for j, obj in enumerate(road):
            if obj == "S":
                get_start_index = True
                break
        if get_start_index:
            break
    
    for route in routes:
        direction, distance = route.split(" ")
        distance = int(distance)
        
        if direction == "E":
            if j + distance >= W or "X" in park[i][j + 1:j + 1 + distance]:
                continue
            j += distance
        elif direction == "W":
            if j - distance < 0 or "X" in park[i][j - distance:j]:
                continue
            j -= distance
        elif direction == "N":
            if i - distance < 0 or "X" in [park[idx][j] for idx in range(i - distance, i)]:     
                continue
            i -= distance
        elif direction == "S":
            if i + distance >= H or "X" in [park[idx][j] for idx in range(i + 1, i + 1 + distance)]:
                continue
            i += distance
            
                
    return [i, j]