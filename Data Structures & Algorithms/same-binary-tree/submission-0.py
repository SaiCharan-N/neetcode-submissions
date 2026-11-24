# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(curr1,curr2):
            if not curr1 and not curr2 :
                return True
            if (curr1 and not curr2 ) or (not curr1 and curr2):
                return False
            if curr1 and curr2 and curr1.val!=curr2.val:
                return False
            a=False
            b=False
            a=same(curr1.left,curr2.left)
            b=same(curr1.right,curr2.right)
            return True if a and b else False
        return same(p,q)