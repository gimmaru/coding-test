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

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left > right:
                return -1
            
            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
            return binary_search(left, right)
        
        return binary_search(0, len(nums) - 1)

'''
* 책에 나온 풀이
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = left + (right - left) // 2
                
                if target > nums[mid]:
                    return binary_search(mid + 1, right)
                elif target < nums[mid]:
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1
        
        return binary_search(0, len(nums) - 1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1