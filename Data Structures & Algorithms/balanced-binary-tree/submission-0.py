# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (True, -1)
            
            left_ok, left_height = dfs(node.left)
            right_ok, right_height = dfs(node.right)

            current_ok = left_ok and right_ok and abs(left_height - right_height) <= 1
            return (current_ok, max(left_height, right_height) + 1)
        
        ok, _ = dfs(root)

        return ok