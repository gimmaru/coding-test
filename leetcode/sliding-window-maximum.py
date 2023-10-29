import sys
import heapq
import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result, priority_q = [], []
        window = collections.deque()
        maximum, max_idx = -sys.maxsize, 0

        for idx, num in enumerate(nums):
            window.append((num, idx))
            heapq.heappush(priority_q, (-num, idx))

            if num > maximum:
                maximum, max_idx = num, idx
            
            if idx < k-1:
                continue
            
            current, win_idx = window.popleft()

            while max_idx < win_idx or win_idx + k - 1 < max_idx:
                maximum, max_idx = heapq.heappop(priority_q)
                maximum = -maximum

            result.append(maximum)

        return result

# 리트코드에서 찾은 풀이
class Solution:
    def maxSlidingWindow(self, nums, k):
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            # 인덱스를 저장하는 큐의 맨 앞의 값은 항상 최댓값이 되도록 설정
            while d and nums[d[-1]] < n:
                d.pop()
            
            # 인덱스 저장
            d += i, 
            
            # 윈도우 사이즈(k)를 초과할 때 맨 처음 들어온 값 방출
            if d[0] == i - k:
                d.popleft()
            
            # 윈도우 사이즈(k)를 만족한 시점 이후로 윈도우의 최댓값을 추가
            if i >= k - 1:
                out += nums[d[0]],
        return out
    
# 답지 풀이 (Time Limit Exceeded)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = collections.deque()
        result = []
        maximum = -sys.maxsize

        for idx, num in enumerate(nums):
            window.append(num)

            if idx < k-1:
                continue
            
            if maximum == -sys.maxsize:
                maximum = max(window)
            elif num > maximum:
                maximum = num
            
            result.append(maximum)

            if maximum == window.popleft():
                maximum = -sys.maxsize

        return result