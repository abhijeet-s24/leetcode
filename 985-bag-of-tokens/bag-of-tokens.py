class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        left,right=0,len(tokens)-1
        score,ans=0,0
        while left<=right:
            if power>=tokens[left]:
                power-=tokens[left]
                score+=1
                left+=1
                ans=max(ans,score)
            elif score>0 and left<right:
                power+=tokens[right]
                score-=1
                right-=1
            else: break
        return ans