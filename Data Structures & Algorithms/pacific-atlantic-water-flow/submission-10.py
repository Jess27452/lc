class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        
        if not heights or not heights[0]:
            return []
        atl=[[False]*cols for _ in range(rows)]
        pac=[[False]*cols for _ in range(rows)]
        res=[]
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        def bfs(source,ocean):
            q=deque()
            for r,c in source:
                ocean[r][c]=True
                q.append((r,c))
            while q:
                r,c=q.popleft()
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if (nr in range(rows) and nc in range(cols) and ocean[nr][nc]==False and heights[nr][nc]>=heights[r][c]):
                            q.append([nr,nc]) 
                            ocean[nr][nc]=True
        pacific=[]
        atlantic=[]
        for i in range(cols):
            pacific.append((0,i))
            atlantic.append((rows-1,i))
        for j in range(rows):
            pacific.append((j,0))
            atlantic.append((j,cols-1))
        bfs(pacific,pac)
        bfs(atlantic,atl)

        for r in range(rows):
            for c in range(cols):
                if pac[r][c]==True and atl[r][c]==True:
                    res.append([r,c])
        return res




        