from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = []

        def dfs(node):
            if not node:
                return 0
            
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            result.append(abs(left_depth - right_depth) < 2)
            return max(left_depth, right_depth) + 1
        
        dfs(root)
        return all(result)

'''
* 책에 나온 풀이
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 0
            
            left = check(root.left)
            right = check(root.right)

            if left == -1 or \
                right == -1 or \
                abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        
        return check(root) != -1