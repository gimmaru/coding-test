from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        subset = []
        def dfs(nums):
            for i, num in enumerate(nums):
                subset.append(num)
                result.append(subset[:])
                dfs(nums[i+1:])
                subset.pop()
        
        dfs(nums)
        return result

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        subset = []
        def dfs(index):
            for i in range(index, len(nums)):
                subset.append(nums[i])
                result.append(subset[:])
                dfs(i + 1)
                subset.pop()
        
        dfs(0)
        return result

'''
* 책에 나온 풀이
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(index, subset):
            result.append(subset)

            for i in range(index, len(nums)):
                dfs(i + 1, subset + [nums[i]])
        
        dfs(0, [])
        return result