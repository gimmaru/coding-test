from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    longest: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def dfs(node):
            if node is None:
                return -1
            
            left = dfs(node.left) + 1
            right = dfs(node.right) + 1
            
            if node.right is None and node.left is None:
                return 0
            if node.right is None and node.left.val == node.val:
                self.longest = max(self.longest, left)
                return left
            if node.left is None and node.right.val == node.val:
                self.longest = max(self.longest, right)
                return right
            if node.right is not None and node.left is not None:
                if node.left.val == node.val and node.right.val == node.val:
                    self.longest = max(self.longest, left + right)
                    return max(left, right)
                if node.left.val == node.val:
                    self.longest = max(self.longest, left)
                    return left
                if node.right.val == node.val:
                    self.longest = max(self.longest, right)
                    return right
            return 0
        dfs(root)
        return self.longest

'''
* 책에 나온 풀이
'''

class Solution:
    longest: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            
            self.longest = max(self.longest, left + right)
            return max(left, right)
        
        dfs(root)
        return self.longest