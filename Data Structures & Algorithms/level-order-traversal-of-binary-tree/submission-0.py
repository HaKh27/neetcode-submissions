# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque([root])
        result=[]
        while queue: 
            levels=[]
            for i in range(len(queue)): 
                node= queue.popleft()
                if node is not None: 
                    levels.append(node.val)
                elif not node: 
                    return []
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
            result.append(levels)
        
        return result 
            

        