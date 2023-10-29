class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def calculate(num):
            if num < 2:
                return num
            return num % 2 + calculate(num // 2)
        return calculate(x^y)

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x^y
        dist = 0
        while num > 0:
            dist += num % 2
            num = num // 2
        return dist

'''
* 책에 나온 풀이
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')