class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        x=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]: x[i]=max(x[i],x[j]+1)
        return max(x)
        