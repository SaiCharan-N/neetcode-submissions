# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=deque([])
        queue.append(root)
        result=[]
        while queue:
            b=[]
            for i in range(len(queue)):
                a=queue.popleft()
                if a:
                    b.append(a.val)
                    if  a.left:
                        queue.append(a.left)
                    if a.right:
                        queue.append(a.right)
            result.append(b)
        return result