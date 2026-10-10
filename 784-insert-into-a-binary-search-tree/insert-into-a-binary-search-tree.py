# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, target: int) -> TreeNode | None:
        newNode=TreeNode(target)
        curr=root
        if root==None: return newNode
        while curr!=None:
            if target<curr.val:
                if curr.left!=None: curr=curr.left
                else:
                    curr.left=newNode
                    break
            if target>curr.val:
                if curr.right!=None: curr=curr.right
                else:
                    curr.right=newNode
                    break
        return root