import collections
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        
        while stack:
            node = stack.pop()
            if not node:
                continue
                
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
            node.left, node.right = node.right, node.left
        
        return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return
            node.left, node.right = node.right, node.left
            dfs(node.right)
            dfs(node.left)
            
        dfs(root)
        return root

'''
* 책에 나온 풀이
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = \
                self.invertTree(root.right), self.invertTree(root.left)
            return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)
        
        return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()

            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)
        
        return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()

            if node:
                stack.append(node.left)
                stack.append(node.right)

                node.left, node.right = node.right, node.left
                
        return root