# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(node: Optional[TreeNode]):
    if not node:
        return 0
    
    left_val = dfs(node.left)
    right_val = dfs(node.right)

    return max(left_val, right_val) + 1

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = dfs(root)
        return result