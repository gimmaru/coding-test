def solution(m, n, startX, startY, balls):
    answer = []
    
    def get_distance(x_1, y_1, x_2, y_2):
        a = ( (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 ) ** (1 / 2)
        b = ( (startX - x_2) ** 2 + (startY - y_2) ** 2 ) ** (1 / 2)
        return round( (a + b) ** 2 )
    
    def get_wall(x_1, y_1, x_2, y_2):
            return (x_1 / (x_1 + x_2) * y_2) + (x_2 / (x_1 + x_2) * y_1)
    
    for ball in balls:
        x, y = ball
            
        left = get_distance(x, y, 0, get_wall(x, y, startX, startY))
        right = get_distance(x, y, m, get_wall(m - x, y, m - startX, startY))
        top = get_distance(x, y, get_wall(n - y, x, n - startY, startX), n)
        bottom = get_distance(x, y, get_wall(y, x, startY, startX), 0)

        if startX == x:
            if startY > y:
                distances = [left, right, top]
            else:
                distances = [left, right, bottom]
        elif startY == y:
            if startX > x:
                distances = [right, top, bottom]
            else:
                distances = [left, top, bottom]
        else:
            distances = [left, right, top, bottom]

        answer += min(distances),
        
    return answer


def solution(m, n, startX, startY, balls):
    answer = []

    def get_distance(x, y):
         return x ** 2 + y ** 2
    
    for ball in balls:
        x, y = ball
        sub_x = startX - x
        sub_y = startY - y
        sum_x = startX + x
        sum_y = startY + y

        left = get_distance(sum_x, sub_y)
        right = get_distance(2 * m - sum_x, sub_y)
        top = get_distance(sub_x, 2 * n - sum_y)
        bottom = get_distance(sub_x, sum_y)

        if sub_x == 0:
            if sub_y > 0:
                distances = [left, right, top]
            else:
                distances = [left, right, bottom]
        elif sub_y == 0:
            if sub_x > 0:
                distances = [right, top, bottom]
            else:
                distances = [left, top, bottom]
        else:
            distances = [left, right, top, bottom]
        
        answer += min(distances),
    return answer 