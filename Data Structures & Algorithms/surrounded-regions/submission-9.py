class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()
        def addCell(r, c):
            if(r in range(ROWS) and c in range(COLS) and board[r][c]=="O"):
                board[r][c]="T"
                q.append((r,c))
        for i in range(ROWS):
            addCell(i,0)
            addCell(i,COLS-1)
        for j in range(COLS):
            addCell(0,j)
            addCell(ROWS-1,j)
        while q:
            r, c = q.popleft()

            addCell(r + 1, c)
            addCell(r - 1, c)
            addCell(r, c + 1)
            addCell(r, c - 1)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="T":
                    board[i][j]="O"
                
                    


                