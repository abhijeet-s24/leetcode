class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        ans=0
        for cost in costs:
            if coins>=cost: 
                coins-=cost
                ans+=1
        return ans