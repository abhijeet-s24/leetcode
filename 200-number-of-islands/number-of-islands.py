class Solution:
    def numIslands(self, mat: List[List[str]]) -> int:
        n,m=len(mat),len(mat[0])
        count=0
        visit=[[0 for _ in range(m)]for _ in range(n)]
        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=m or visit[i][j]==1 or mat[i][j]=="0": return
            # mat[i][j]=0
            visit[i][j]=1
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        for i in range(n): 
            for j in range(m):
                if mat[i][j]=="1" and visit[i][j]==0: 
                    count+=1
                    dfs(i,j)
        return count