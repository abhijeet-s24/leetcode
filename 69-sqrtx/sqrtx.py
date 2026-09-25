class Solution:
    def mySqrt(self, x: int) -> int:
        # if 1<=x<4: return 1
        # elif  4<=x<9: return 2
        if x<2: return x
        left,right=1,x
        ans=0
        while left<=right:
            mid=(left+right)//2
            if mid*mid<=x: 
                ans=mid
                left=mid+1
            else: right=mid-1
        return ans