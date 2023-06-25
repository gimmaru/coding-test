class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack, table = list(), dict()
        for char in s:
            if char not in table:
                table[char] = 1
            else:
                table[char] += 1
        
        for char in s:
            if char in stack:
                table[char] -= 1
                continue

            while stack and stack[-1] > char:
                if table[stack[-1]] > 0:
                    stack.pop()
                else:
                    break
            
            stack.append(char)
            table[char] -= 1
                
        return ''.join(stack)
