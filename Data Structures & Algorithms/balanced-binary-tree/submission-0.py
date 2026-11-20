# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        def post_order(root):
            if root is None: 
                return 0 
            
            left= post_order(root.left)
            right= post_order(root.right)

            if left ==-1 or right==-1: 
                return -1

            if abs(left-right)>1:
                return -1 
                
            return 1 + max(left,right)

        height = post_order(root)
        return False if height==-1 else True
        