class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length%2 != 0:
            return False
        
        pair_map = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        stack = list()
        for char in s:
            if char in pair_map:
                stack.append(char)
            elif not stack:
                return False
            elif pair_map[stack.pop()] != char:
                return False
        
        return False if stack else True
