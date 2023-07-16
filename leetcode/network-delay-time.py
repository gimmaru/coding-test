import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        network = collections.defaultdict(list)
        for u, v, t in times:
            network[u].append((t, v))
        
        queue = []
        for v in network[k]:
            heapq.heappush(queue, v)
        traced = {k}

        while queue:
            prev_t, v = heapq.heappop(queue)
            if v in traced:
                continue
            
            traced.add(v)
            if len(traced) == n:
                return prev_t

            for t, w in network[v]:
                heapq.heappush(queue, (prev_t + t, w))
        
        return -1


'''
* 책에 나온 풀이
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        Q = [(0, k)]
        dist = collections.defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        
        if len(dist) == n:
            return max(dist.values())
        return -1