import collections
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = collections.Counter(nums)
        return [key for key, freq in table.most_common(k)]