# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0
            a=1
            b=1
            if node.left:
                a=1+depth(node.left)
            if node.right:
                b=1+depth(node.right)
            return max(a,b)
        return depth(root)
        