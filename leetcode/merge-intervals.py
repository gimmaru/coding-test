import collections
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if isinstance(intervals, list):
            intervals.sort()
        
        intervals = collections.deque(intervals)
        merged = intervals.popleft()
        merge_count = 0

        for _ in range(len(intervals)):
            inter = intervals.popleft()
            if merged[1] >= inter[1]:
                merge_count += 1
            elif merged[1] >= inter[0]:
                merged = [merged[0], inter[1]]
                merge_count += 1
            else:
                intervals.append(merged)
                merged = inter
        intervals.append(merged)

        if not merge_count:
            return intervals

        return self.merge(intervals)

'''
* 책에 나온 풀이
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,
        return merged