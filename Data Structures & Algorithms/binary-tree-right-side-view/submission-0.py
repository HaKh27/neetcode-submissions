# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result=[]
        queue= deque([root])
        while queue: 
            rightMost=None 
            for i in range(len(queue)):
                node= queue.popleft()
    
                if node: 
                    rightMost=node
                    queue.append(node.left)
                    queue.append(node.right)
            
            if rightMost: 
                result.append(rightMost.val)
        
        return result 
