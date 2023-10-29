class Solution:
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF

    def getSum(self, a: int, b: int) -> int:
        a, b = (a ^ b) & self.MASK, ((a & b) << 1) & self.MASK
        
        if not b:
            if a > self.INT_MAX:
                a = ~(a ^ self.MASK)
            return a
        
        return self.getSum(a, b)


'''
* 책에 나온 풀이
'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        
        while b:
            a, b = (a^b) & MASK, ((a&b) << 1) & MASK
        
        if a > INT_MAX:
            a = ~(a^MASK)
        return a