from typing import List
import itertools


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(elements):
            if len(prev_elements) == k:
                result.append(prev_elements[:])
                return

            for i, e in enumerate(elements, 1):
                prev_elements.append(e)
                dfs(elements[i:])
                prev_elements.pop()
        
        result, prev_elements = [], []
        elements = list(range(1, n+1))
        dfs(elements)
        
        return result

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        elements = list(range(1, n+1))
        return list(map(list, itertools.combinations(elements, k)))

'''
* 책에 나온 풀이
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return
            
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()
        
        dfs([], 1, k)
        return results