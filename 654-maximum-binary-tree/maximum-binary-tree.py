# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        def build(left,right):
            if left>right: return None
            maxInd=left
            for i in range(left+1,right+1):
                if nums[i]>nums[maxInd]: maxInd=i
            root=TreeNode(nums[maxInd])
            root.left=build(left,maxInd-1)
            root.right=build(maxInd+1,right)
            return root
        return build(0,len(nums)-1)