class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0: return 0
        m = len(grid) ; n = len(grid[0])
        total = [[0 for _ in range(n)] for _ in range(m)]
        visit = [[0]*n for _ in range(m)]
        apt = []
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:apt.append([r,c])
        for x,y in apt:
            visited = [[False for _ in range(n)] for _ in range(m)]
            visited[x][y] = True
            open_area = [[x,y,0]]
            count = 1
            while len(open_area):
                r,c,d = open_area.pop(0)
                visit[r][c] +=1
                total [r][c] += d
                dir = [[-1,0],[0,-1],[1,0],[0,1]]
                for p,q in dir:
                    if 0<=r+p<m and 0<=c+q<n and grid[r+p][c+q]!=2 and visited[r+p][c+q] == False:
                        visited[r+p][c+q]=True
                        if grid[r+p][c+q]==0:open_area.append([r+p,c+q,d+1])
                        else:count+=1
            #print(visited)
            if count != len(apt):return -1
        res = -1
        #print(total)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0 and visit[i][j]==count and (res==-1 or total[i][j]<res):
					res = total[i][j]
        return res
                    
            
        
