import sys
import collections
from typing import List

# Time Limit Exceeded
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for v, w in edges:
            graph[v].append(w)
            graph[w].append(v)
        
        global_min = sys.maxsize
        for v in range(n):
            max_height = [0]
            def check_height(v, height, discovered):
                height += 1
                discovered.add(v)

                max_height[0] = max(max_height[0], height)
                for w in graph[v]:
                    if w not in discovered:
                        check_height(w, height, discovered)
            
            check_height(v, 0, set())

            if global_min > max_height[0]:
                global_min = max_height[0]
                result = [v]
            elif max_height[0] == global_min:
                if result:
                    result.append(v)
                else:
                    result = [v]
        return result

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for v, w in edges:
            graph[v].append(w)
            graph[w].append(v)
        
        global_min = sys.maxsize

        for v in range(n):
            queue = collections.deque(graph[v])
            discovered = {v}
            height = 0

            while queue:
                height += 1
                for _ in range(len(queue)):
                    new_v = queue.popleft()
                    discovered.add(new_v)
                    for w in graph[new_v]:
                        if w not in discovered:
                            queue.append(w)

            if global_min > height:
                global_min = height
                result = [v]
            elif global_min == height:
                result.append(v)

        return result

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for v, w in edges:
            graph[v].append((w, 0))
            graph[w].append((v, 0))
        
        global_min = sys.maxsize
        
        for v in range(n):
            stack = graph[v][:]
            max_height = 0
            discovered = {v}

            while stack:
                new_v, height = stack.pop()
                discovered.add(new_v)
                max_height = max(max_height, height)

                if height > global_min:
                    break

                for w, _ in graph[new_v]:
                    if w not in discovered:
                        stack.append((w, height + 1))

            if global_min > max_height:
                global_min = max_height
                result = [v]
            elif global_min == max_height:
                result.append(v)
        return result

'''
* 책에 나온 풀이
'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]

        tree = collections.defaultdict(set)
        for v, w in edges:
            tree[v].add(w)
            tree[w].add(v)
        
        leaves = [k for k, v in tree.items() if len(v) == 1]
        while n > 2:
            n -= len(leaves)

            new_leaves = []
            for leaf in leaves:
                parent = tree[leaf].pop()
                tree[parent].remove(leaf)

                if len(tree[parent]) == 1:
                    new_leaves.append(parent)
            
            leaves = new_leaves

        return leaves