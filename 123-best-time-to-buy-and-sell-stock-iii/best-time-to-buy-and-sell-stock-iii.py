class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        dp=[[[-1]*2 for _ in range(3)] for _ in range(n)]
        def f(i,hold,trans):
            if i==n: return 0
            if trans==2: return 0
            if dp[i][trans][hold]!=-1: return dp[i][trans][hold]
            profit = 0
            skip = f(i+1,hold,trans)
            profit = max(profit,skip)
            if hold==0:
                buy=(-prices[i])+f(i+1,1,trans)
                profit=max(buy,profit)
            else:
                sell=(prices[i])+f(i+1,0,trans+1)
                profit=max(sell,profit)
            dp[i][trans][hold]=profit
            return dp[i][trans][hold]
        return f(0,0,0)