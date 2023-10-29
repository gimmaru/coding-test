def solution(wallpaper):
    start_i, start_j = len(wallpaper), len(wallpaper[0])
    end_i, end_j = 0, 0
    
    for i, row in enumerate(wallpaper):
        for j, file in enumerate(row):
            if '#' == file:
                start_i = min(start_i, i)
                start_j = min(start_j, j)
                end_i = max(end_i, i)
                end_j = max(end_j, j)
                
    return [start_i, start_j, end_i + 1, end_j + 1]