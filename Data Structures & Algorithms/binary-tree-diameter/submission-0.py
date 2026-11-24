# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        seen=0
        def diameter(node):
            nonlocal seen
            if not node:
                return 0
            a=0
            b=0
            if node.left:
                a=1+diameter(node.left)
            if node.right:
                b=1+diameter(node.right)
            if seen<a+b:
                seen=a+b
            return max(a,b) 
        diameter(root)
        return seen