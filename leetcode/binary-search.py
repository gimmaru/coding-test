from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            result = nums.index(target)
        except ValueError:
            result = -1
        return result
