import collections
from typing import List


class Solution:
    def merge(self, left: List, right: collections.deque) -> List:
        idx = 0
        while right:
            r_val = right.popleft()
            while idx < len(left) and left[idx] < r_val:
                idx += 1

            left = left[:idx] + [r_val] + left[idx:]
        
        return left

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def merge_sort(nums):
            length = len(nums)

            if length == 1:
                return nums
            
            mid = length // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])

            return self.merge(left, collections.deque(right))
        
        for idx, num in enumerate(merge_sort(nums)):
            nums[idx] = num

'''
* 책에 나온 풀이
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)

        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1