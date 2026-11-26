class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10: return False
        n-=10
        remove=9
        alice=False
        while n>=remove and remove>0:
            n-=remove
            remove-=1
            alice=not alice
        return not alice