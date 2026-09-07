class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for _ in range(n)]
        ans=[]
        def safe(row,col):
            # cols mein check
            i=row
            while i>=0:
                if board[i][col]=='Q': return False
                i-=1
            # left diagonal check
            i,j=row,col
            while i>=0 and j>=0:
                if board[i][j]=='Q': return False
                i-=1
                j-=1
            # right diagonal check
            i,j=row,col
            while i>=0 and j<n:
                if board[i][j]=='Q': return False
                i-=1
                j+=1
            return True
        def f(row):
            if row==n: 
                ans.append(["".join(r) for r in board])
                return 
            for col in range(n):
                if safe(row,col):
                    board[row][col]='Q'
                    f(row+1)
                    board[row][col]='.'
        f(0)
        return ans