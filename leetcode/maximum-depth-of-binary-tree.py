import collections
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth = [0]
        def dfs(node, depth):
            max_depth[0] = max(max_depth[0], depth)

            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)

        dfs(root, 1)
        return max_depth[0]

# BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = collections.deque([(root, 1)])
        max_depth = 0

        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            
            if node.right:
                queue.append((node.right, depth + 1))
            if node.left:
                queue.append((node.left, depth + 1))

        return max_depth

'''
* 책에 나온 풀이
  반복 구조 BFS
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)

        return depth