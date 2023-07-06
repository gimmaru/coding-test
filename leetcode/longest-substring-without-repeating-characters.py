class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        window_size = len(s)
        while len(set(s)) == len(set(s[:window_size//2])):
            window_size = window_size//2
        s = s[:window_size]

        while window_size:
            for bow in range(len(s) - window_size + 1):
                window = s[bow : window_size+bow]
                if window_size == len(set(window)):
                    return window_size
            window_size -= 1
        
        return window_size


'''
* 책에 나온 풀이
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = dict()
        max_length = start = 0

        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)
            
            used[char] = index
        
        return max_length