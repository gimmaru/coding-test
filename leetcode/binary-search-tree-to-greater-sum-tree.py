# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    accum_sum = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        self.bstToGst(root.right)
        self.accum_sum += root.val
        root.val = self.accum_sum
        self.bstToGst(root.left)
        
        return root

'''
* 책에 나온 풀이
'''
class Solution:
    val: int = 0
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
        
        return root