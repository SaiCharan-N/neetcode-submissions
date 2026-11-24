# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def find(curr,p,q):
            if not curr:
                return False
            if p and curr.val==p.val:
                return curr
            if q and curr.val==q.val:
                return curr
            a=find(curr.left,p,q)
            b=find(curr.right,p,q)
            if a and b:
                return curr
            else:
                return a if a else b
        return find(root,p,q)