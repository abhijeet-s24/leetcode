class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        n=len(nums)
        sums=sum(nums)
        if n==1: return False
        if sums%2!=0: return False
        dp=[[-1 for j in range((sums//2)+1 )] for i in range(n)]
        def f(i,sum1,nums,sums,dp):
            if sum1>(sums//2): return False
            elif sum1==(sums//2): return True
            elif i==n: return False
            if dp[i][sum1]!=-1: return dp[i][sum1]
            take=f(i+1,sum1+nums[i],nums,sums,dp)
            not_take=f(i+1,sum1,nums,sums,dp)
            dp[i][sum1]=take or not_take
            return dp[i][sum1]
        return f(0,0,nums,sums,dp)