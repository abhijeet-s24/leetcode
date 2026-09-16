class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq={}
        ans=[]
        for num in nums:
            if num in freq: freq[num]+=1
            else: freq[num]=1
            if freq[num]==2: ans.append(num)
        return ans