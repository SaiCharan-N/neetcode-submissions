# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue=deque([])
        queue.append(root)
        result=[]
        while queue:
            level=[]
            for i in range(len(queue)):
                a=queue.popleft()
                if a:
                    level.append(a.val)
                    queue.append(a.left)
                    queue.append(a.right)
            if level:
                result.append(level)
        ans=[]
        for i in range(len(result)):
            ans.append(result[i][-1])
        return ans 