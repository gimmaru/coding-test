def solution(grid):
    m, n = len(grid) - 1, len(grid[0]) - 1
    
    # up, down, left, right
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    Left = {
        (1, 0): (0, -1),
        (0, 1): (1, 0),
        (-1, 0): (0, 1),
        (0, -1): (-1, 0),
    }
    Right = {
        (1, 0): (0, 1),
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
        (0, -1): (1, 0)
    }

    answer = []
    trace = set()
    for direction in directions:
        r, c = 0, 0
        start, count = (r, c, direction), 0
        if start in trace:
            continue
        trace.add(start)
        
        while True:
            r += direction[0]
            c += direction[1]
            count += 1

            if r < 0:
                r = m
            elif r > m:
                r = 0
            
            if c < 0:
                c = n
            elif c > n:
                c = 0
            
            if grid[r][c] == "S":
                pass
            elif grid[r][c] == "L":
                direction = Left[direction]
            elif grid[r][c] == "R":
                direction = Right[direction]

            if (r, c, direction) == start:
                answer.append(count)
            
            trace.add( (r, c, direction) )

    return sorted(answer)


def move(r, c, d):
    global directions, n, m
    dx, dy = directions[d]
    return (r + dx) % n , (c + dy) % m

def rotate(d, node):
    if node == 'R':
        d = (d + 1) % 4
    elif node == 'L':
        d = (d - 1) % 4
    return d

def solution(grid):
    global n, m, answer, directions
    answer = []
    n, m = len(grid), len(grid[0])
    visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
    directions = [[1, 0], [0, -1], [-1, 0], [0, 1]] # D, L, U, R
    
    for r in range(n):
        for c in range(m):
            for d in range(4):
                if not visited[r][c][d]:
                    cx, cy, cd = r, c, d
                    cnt = 0
                    while not visited[cx][cy][cd]:
                        visited[cx][cy][cd] = True
                        cnt += 1
                        cx, cy = move(cx, cy, cd)
                        cd = rotate(cd, grid[cx][cy])
                    answer.append(cnt)
    return sorted(answer)