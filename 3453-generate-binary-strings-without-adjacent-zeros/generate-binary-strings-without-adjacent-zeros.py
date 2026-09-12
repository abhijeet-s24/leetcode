class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans=[]
        def solve(s):
            if len(s)==n: 
                ans.append(s)
                return 
            solve(s+"1")
            if len(s)==0 or s[-1]=="1": solve(s+"0")
        solve("")
        return ans