import collections
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        criterion = len(nums) // 2 + 1
        freq = collections.defaultdict(int)
        
        for num in nums:
            freq[num] += 1
            if freq[num] >= criterion:
                return num


# 답지 풀이
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)
            
            if counts[num] > len(nums) // 2:
                return num

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]