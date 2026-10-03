class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        alt,maxAlt=0,0
        for x in gain:
            alt+=x
            maxAlt=max(maxAlt,alt)
        return maxAlt