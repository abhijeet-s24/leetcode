# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans=0
        def dfs(node):
            nonlocal ans
            if node==None: return 0,0
            left_sum,left_count=dfs(node.left)
            right_sum,right_count=dfs(node.right)
            sums=left_sum+right_sum+node.val
            count=left_count+right_count+1
            avg=sums//count
            if node.val==avg: ans+=1
            return sums,count
        dfs(root)
        return ans