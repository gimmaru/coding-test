def get_bit_array(n, r, array=[1], one=[1, 1, 0, 1, 1], zero=[0, 0, 0, 0, 0]):
    if n == 0:
        return array
    
    next_array = []
    for bit in array:
        if bit == 1:
            next_array.extend(one)
        else:
            next_array.extend(zero)
        
        if len(next_array) >= r:
            return get_bit_array(0, r, next_array)
            
    return get_bit_array(n-1, r, next_array)

def solution(n, l, r):
    one = [1, 1, 0, 1, 1]
    zero = [0, 0, 0, 0, 0]
    array, index = [1, 1, 0, 1, 1], 0
    l += 4
    r += 5
    
    while len(array) < r + 1:
        if array[index] == 1:
            array.extend(one)
        else:
            array.extend(zero)
        index += 1
    
    return sum(array[l:r])

from sklearn