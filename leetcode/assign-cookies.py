import collections
import bisect
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g, s = collections.deque(g), collections.deque(s)
        next_g = True
        answer = 0
        maximum = len(g)

        while s and answer < maximum:
            if next_g:
                curr_g = g.popleft()
                next_g = False

            curr_s = s.popleft()
            if curr_g <= curr_s:
                answer += 1
                next_g = True

        return answer
    
# 답지 풀이
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child_i = cookie_j = 0
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1
        return child_i

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        result = 0
        for i in s:
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1
        return result