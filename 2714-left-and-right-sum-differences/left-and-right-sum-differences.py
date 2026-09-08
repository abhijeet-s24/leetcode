class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total=sum(nums)
        left=0
        ans=[]
        for num in nums:
            right=total-num-left
            ans.append(abs(left-right))
            left+=num
        return ans