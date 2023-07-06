import copy
import itertools
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)

        def dfs(nums, discover=[]):
            if len(discover) == length:
                result.append(discover)
                return
            
            for num in nums:
                new_discover = copy.deepcopy(discover)
                new_nums = copy.deepcopy(nums)

                new_discover.append(num)
                new_nums.remove(num)
                
                dfs(new_nums, new_discover)
        
        dfs(nums)
        return result

'''
* 책에 나온 풀이
prev_elements로 공간복잡도 낮춤
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])
            
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop() # ***
        
        dfs(nums)
        return result

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, itertools.permutations(nums)))