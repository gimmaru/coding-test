import sys
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        starts = collections.deque()
        remove_cands = collections.deque()
        T = collections.Counter(t)
        start, end = None, None
        flag = False
        minimum = sys.maxsize
        result = ""

        indices_map = collections.defaultdict(collections.deque)
        for i, char in enumerate(s):
            if char in T:
                if not flag:
                    starts += i,
                    indices_map[char] += i,
                    if T[char]:
                        T[char] -= 1
                    elif s[start] == char:
                        start = i
                    if start is None:
                        start = i
                    end = i

                    flag = not any(T.values())
                
                if flag:
                    if end - start < minimum:
                        result = s[start:end+1]
                        minimum = end - start

                    poped = indices_map[char].popleft()
                    indices_map[char] += i,
                    starts += i,

                    remove_cands += poped,
                    while remove_cands and remove_cands[-1] == starts[0]:
                        starts.popleft()
                        remove_cands.pop()
                    
                    start = starts[0]
                    end = i

                    if end - start < minimum and end - start >= len(t)-1:
                        result = s[start:end+1]
                        minimum = end - start

        return result

# 답지 풀이
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0

        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                if not end or right - left <= end - start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1
        return s[start:end]

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    sol = Solution()
    print(sol.minWindow(s, t))