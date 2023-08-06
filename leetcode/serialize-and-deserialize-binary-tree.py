import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'

        data = '['
        Q = collections.deque([root])
        
        while Q:
            node = Q.popleft()
            if node:
                data += str(node.val)
                Q.append(node.left)
                Q.append(node.right)
            else:
                data += 'null'
            data += ','

        return data[:-1] + ']'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return
        values = collections.deque(data[1:-1].split(','))
        val = values.popleft()
        root = TreeNode(val)
        Q = collections.deque([root])

        while Q:
            node = Q.popleft()
            left = values.popleft()
            right = values.popleft()

            if left != 'null':
                node.left = TreeNode(left)
                Q.append(node.left)
            
            if right != 'null':
                node.right = TreeNode(right)
                Q.append(node.right)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

'''
* 책에 나온 풀이
'''
class Codec:
    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque([root])
        result = ['#']

        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)
        
    def deserialize(self, data: str) -> TreeNode:
        if data == '##':
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2

        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root