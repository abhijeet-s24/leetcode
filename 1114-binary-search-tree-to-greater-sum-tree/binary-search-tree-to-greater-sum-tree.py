# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total=[0]
        def inorder(node):
            if node is None: return 
            inorder(node.right)
            total[0]+=node.val
            node.val=total[0]
            inorder(node.left)
        inorder(root)
        return root