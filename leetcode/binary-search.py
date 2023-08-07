from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            result = nums.index(target)
        except ValueError:
            result = -1
        return result

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return -1