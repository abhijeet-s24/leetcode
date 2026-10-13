class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[-1 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        def f(i,j,text1,text2):
            if i>=len(text1) or j>=len(text2): return 0
            if dp[i][j]!=-1: return dp[i][j]
            ans=0
            if text1[i]==text2[j]: ans=1+f(i+1,j+1,text1,text2)
            else: ans=max(f(i+1,j,text1,text2),f(i,j+1,text1,text2))
            dp[i][j]=ans
            return dp[i][j]
        return f(0,0,text1,text2)