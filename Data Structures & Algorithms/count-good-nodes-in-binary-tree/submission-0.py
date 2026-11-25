# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 


        def dfs(root, best): 
            if not root: 
                return 0 
            
            result= 1 if root.val>=best else 0 
            best= max(best, root.val)
            result+= dfs(root.left, best)
            result+= dfs(root.right, best)

            return result 
        
        return dfs(root, root.val)

        