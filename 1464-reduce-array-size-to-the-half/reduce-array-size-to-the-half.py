class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        freq={}
        for x in arr:
            freq[x]=freq.get(x,0)+1
        items=[]
        for num,f in freq.items():
            items.append((num,f))
        items.sort(key=lambda x:-x[1])
        size=len(arr)
        count=0
        for x in items:
            size-=x[1]
            count+=1
            if size<=len(arr)//2: return count