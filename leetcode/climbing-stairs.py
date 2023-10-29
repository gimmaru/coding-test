import collections


class Solution:
    def climbStairs(self, n: int) -> int:
        factorial = [1]
        for i in range(1, n+1):
            factorial.append(i * factorial[i-1])
        
        def combine(n, r, factorial):
            return int(factorial[n] / (factorial[n-r] * factorial[r]))
        
        max_two = n // 2
        result = 0
        for i in range(max_two + 1):
            result += combine(n - i, i, factorial)
        return result
    

# 답지 풀이
class Solution:
    dp = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2) 
        return self.dp[n]