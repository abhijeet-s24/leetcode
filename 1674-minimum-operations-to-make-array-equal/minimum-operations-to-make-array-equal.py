class Solution:
    def minOperations(self, n: int) -> int:
        arr=[]
        for i in range(n):
            arr.append((2*i)+1)
        tar=(arr[0]+arr[n-1])//2
        ans=0
        for i in arr:
            ans+=abs(tar-i)
        return ans//2