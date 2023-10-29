import collections
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for idx, num in enumerate(nums, 3):
            dp += max(num + dp[idx - 2], num + dp[idx - 3]),
        return max(dp)

class Solution:
    def rob(self, nums: List[int]) -> int:
        maximum = float('-inf')
        dp = [0, 0, 0]

        for idx, num in enumerate(nums, 3):
            dp += max(num + dp[idx - 2], num + dp[idx - 3]),
            maximum = max(maximum, dp[-1])
        return maximum

# 답지 풀이 참고 후 추가
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0]
        for idx, num in enumerate(nums, 2):
            dp += max(dp[idx - 1], num + dp[idx - 2]),
        return dp[-1]
    

# 답지 풀이
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp.popitem()[1]