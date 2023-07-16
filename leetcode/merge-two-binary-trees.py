from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
            
        def dfs(node1, node2):
            if not node1 and not node2:
                return
            
            if node1 and node2:
                node1.val += node2.val
                if not node1.right and node2.right:
                    node1.right = TreeNode()
                if not node1.left and node2.left:
                    node1.left = TreeNode()

                dfs(node1.left, node2.left)
                dfs(node1.right, node2.right)
        
        dfs(root1, root2)
        return root1

'''
* 책에 나온 풀이
'''
class Solution:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)

            return node
        else:
            return t1 or t2