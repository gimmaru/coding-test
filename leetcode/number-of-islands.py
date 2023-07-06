from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        num_islands = 0
        discovered = dict()

        def search_island(i, j):
            queue = deque([(i, j)])
            while queue:
                i, j = queue.popleft()
                search_spaces = [
                    (i-1, j), (i+1, j),
                    (i, j-1), (i, j+1)
                ]
                for new_i, new_j in search_spaces:
                    if new_i == -1 or new_j == -1 or new_i == m or new_j == n:
                        continue

                    if (new_i, new_j) not in discovered:
                        w = grid[new_i][new_j]
                        discovered[(new_i, new_j)] = 0
                        if w == "1":
                            queue.append((new_i, new_j))

        for i in range(m):
            for j in range(n):
                if (i, j) not in discovered:
                    discovered[(i, j)] = 0
                    v = grid[i][j]
                    if v == "1":
                        num_islands += 1
                        search_island(i, j)

        return num_islands
    
'''
* 책에 나온 풀이
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i == -1 or j == -1 or \
                i == m or j == n or \
                grid[i][j] != '1':
                return
            
            grid[i][j] = '0'
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    result += 1
        
        return result