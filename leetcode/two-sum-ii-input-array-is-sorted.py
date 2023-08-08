import collections
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = collections.deque(numbers)
        idx_a = 0

        while nums:
            idx_a += 1
            L = nums.popleft()
            T = target - L

            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] < T:
                    left = mid + 1
                elif nums[mid] > T:
                    right = mid - 1
                else:
                    return [idx_a, idx_a + mid + 1]


'''
* 책에 나온 풀이
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left != right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left + 1, right + 1
            

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            left, right = k + 1, len(numbers) - 1
            expected = target - v

            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return k + 1, mid + 1


import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, lo=k + 1)
            if len(numbers) > i and numbers[i] == expected:
                return k + 1, i + 1