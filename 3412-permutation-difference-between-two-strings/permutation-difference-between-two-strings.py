class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        pos={}
        for i in range(len(s)):
            pos[s[i]]=i
        ans=0
        for i in range(len(t)):
            ans+=abs(pos[t[i]]-i)
        return ans