class Solution:
    def frequencySort(self, s: str) -> str:
        x={}
        for ch in s:
            x[ch]=x.get(ch,0)+1
        l=[]
        for ch in x:
            l.append((ch,x[ch]))
        l.sort(key=lambda x: x[1], reverse=True)
        ans=""
        for ch, freq in l:
            ans+=ch*freq
        return ans
        # freq=Counter(s)
        # first=max(freq.values())