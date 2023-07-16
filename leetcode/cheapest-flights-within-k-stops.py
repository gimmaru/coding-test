import heapq
import collections
from collections import defaultdict, deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for _from, to, price in flights:
            graph[_from].append((price, to))
        
        dist_to_price = dict()
        queue = deque([(0, src, 0)])

        while queue:
            depth, _from, price = queue.popleft()

            if _from not in dist_to_price or price < dist_to_price[_from]:
                dist_to_price[_from] = price

                if depth <= k:
                    for extra_p, to in graph[_from]:
                        queue.append((depth + 1, to, price + extra_p))

        return dist_to_price[dst] if dst in dist_to_price else -1

'''
* 책에 나온 풀이
(Time Limit Exceeded)
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        Q = [(0, src, K)]

        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))
        return -1