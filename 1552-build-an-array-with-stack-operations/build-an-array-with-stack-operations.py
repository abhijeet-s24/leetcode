class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        curr=1
        for x in target:
            while curr<x:
                ans.append("Push")
                ans.append("Pop")
                curr+=1
            ans.append("Push")
            curr+=1
        return ans