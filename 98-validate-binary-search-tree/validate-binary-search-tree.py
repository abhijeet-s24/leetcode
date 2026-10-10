# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def check(root,mini,maxi):
            if root==None: return True
            if root.val<mini or root.val>maxi: return False
            checkLeft=check(root.left,mini,root.val-1)
            checkRight=check(root.right,root.val+1,maxi)
            return checkLeft and checkRight
        return check(root,float("-inf"),float("inf"))