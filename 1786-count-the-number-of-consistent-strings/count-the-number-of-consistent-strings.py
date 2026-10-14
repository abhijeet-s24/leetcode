class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed=set(allowed)
        ans=0
        for word in words:
            valid=True
            for ch in word:
                if ch not in allowed: 
                    valid=False
                    break
            if valid: ans+=1
        return ans