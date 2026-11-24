class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        q=deque()
        f=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1: f+=1
                elif grid[i][j]==2: q.append([i,j])
        time=0
        direction=[[-1,0],[0,-1],[1,0],[0,1]]
        while q and f>0:
            for i in range(len(q)):
                x,y=q.popleft()
                for dx,dy in direction:
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<n and 0<=ny<m and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        f-=1
                        q.append([nx,ny])
            time+=1
        if f!=0: return -1
        return time