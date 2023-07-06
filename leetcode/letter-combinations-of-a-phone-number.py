from typing import List
import copy

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit2letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        def get_combinations(digits, discovered=[]):
            if not digits:
                return discovered
            
            letters = digit2letters[digits[0]]
            if not discovered:
                discovered = copy.deepcopy(letters)
            else:
                prev_len = len(discovered)
                discovered *= len(letters)
                correction = -1
                for idx in range(len(discovered)):
                    if idx % prev_len == 0:
                        correction += 1
                    discovered[idx] += letters[correction]
                    # print(f"{idx}: {discovered}")
            return get_combinations(digits[1:], discovered)
        
        return get_combinations(digits)

'''
* 책에 나온 풀이
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
            
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)
        
        if not digits:
            return []
            
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        result = []
        dfs(0, "")

        return result