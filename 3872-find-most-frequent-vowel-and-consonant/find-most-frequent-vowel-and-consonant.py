class Solution:
    def maxFreqSum(self, s: str) -> int:
        countA=0
        countE=0
        countI=0
        countO=0
        countU=0
        consonents=[0]*26
        for i in s:
            if i=="a": countA+=1
            elif i=="e": countE+=1
            elif i=="i": countI+=1
            elif i=="o": countO+=1
            elif i=="u": countU+=1
            else: consonents[ord(i)-ord('a')]+=1
        maxVowel=max(countA,countE,countI,countO,countU)
        maxConsnent=max(consonents)
        return maxVowel+maxConsnent