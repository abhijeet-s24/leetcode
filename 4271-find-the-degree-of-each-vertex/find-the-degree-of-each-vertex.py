class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n=len(matrix)
        ans=[]
        for i in range(n):
            deg=0
            for j in range(n):
                deg+=matrix[i][j]
            ans.append(deg)
        return ans