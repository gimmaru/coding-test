from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        prev_elements = []
        def dfs(elements, target):
            if target == 0:
                result.append(prev_elements[:])
                return
            elif target < 0:
                return
            
            for i, e in enumerate(elements):
                prev_elements.append(e)
                dfs(elements[i:], target - e)
                prev_elements.pop()
        
        dfs(candidates, target)
        return result

# combinations 책 풀이를 참고하여 수정한 버전
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(elements, start, target):
            if target == 0:
                result.append(elements[:])
                return
            elif target < 0:
                return
            
            for i in range(start, len(candidates)):
                elements.append(candidates[i])
                dfs(elements, i, target - candidates[i])
                elements.pop()
        
        result = []
        dfs([], 0, target)
        return result

'''
* 책에 나온 풀이
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return
            
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])
        
        dfs(target, 0, [])
        return result