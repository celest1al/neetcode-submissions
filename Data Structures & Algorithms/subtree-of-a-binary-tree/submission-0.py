# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def is_same_tree(tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
    result = False

    if tree1 is None and tree2 is None:
        result = True
    elif tree1 is None or tree2 is None:
        result = False
    elif tree1.val != tree2.val:
        result = False
    elif not is_same_tree(tree1.left, tree2.left):
        result = False
    else:
        result = is_same_tree(tree1.right, tree2.right)
    
    return result


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        result = False
        if subRoot is None:
            result = True
        elif root is None:
            result = False
        elif is_same_tree(root, subRoot):
            result = True
        elif self.isSubtree(root.left, subRoot):
            result = True
        else:
            result = self.isSubtree(root.right, subRoot)
    
        return result


        