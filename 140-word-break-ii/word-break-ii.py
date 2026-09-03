class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans=[]
        def f(i):
            if i==len(s): 
                sentence=" ".join(curr)
                ans.append(sentence)
                return
            for j in range(i,len(s)):
                word=s[i:j+1]
                if word in wordDict:
                    curr.append(word)
                    f(j+1)
                    curr.pop()
        curr=[]
        f(0)
        return ans