import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float('-inf')
        curr_max = 0
        
        for num in nums:
            curr_max += num
            maximum = max(maximum, curr_max)

            if curr_max < 0:
                curr_max = 0

        return maximum
    

# 답지 풀이
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        
        return best_sum